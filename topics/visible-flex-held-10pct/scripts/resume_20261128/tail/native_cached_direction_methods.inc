    // Independent predictor-only cache. The original flow/rhs/full-J methods
    // above are unchanged. No binary64 boundary is introduced at RK stages.
    struct DirectionPoint {
        int point;
        std::vector<R> Q,L,chol;
    };
    std::vector<DirectionPoint> direction_points;
    std::vector<R> direction_final_state;

    std::vector<R> direction_cache_rhs(const std::vector<R>&state,int point,double x) {
        const auto&g=coeff[point];
        auto rt=root(state,g,x);std::vector<R>flux(M,R(0));
        minA=std::min(minA,rt.e.minA);minD=std::min(minD,rt.e.minD);
        for(int n=0;n<nq;n++){
            const auto &v=rt.e.rows[n];R u=g.w2*(R(2)*v.K+v.K*v.K+g.E*v.P*v.P);
            R f=(v.K+u/(R(1)+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd);
            R product=v.U*f;
            for(int j=0;j<M;j++)flux[j]+=product*sn[n*M+j]/nq;
        }
        std::vector<R>out(size,R(0));
        for(int j=0;j<M;j++){
            int m=frequency[j];R p=g.pnum[j]*state[j]/g.pden;
            R linear=-m*rt.L[j+1]+(m*m-1)*p;
            out[j]=g.sigma*((m*m-4)*state[j]+g.qlnum*rt.L[j+1]/g.r3);
            out[M+j]=R(4)*g.sigma*state[M+j]+g.pref*m*(linear+flux[j]);
        }
        out[K]=g.mean*rt.L[0];out[K+1]=g.mean;
        std::vector<R>B(J*J,R(0));for(int i=0;i<J;i++)B[i*J+i]=R(1);
        for(int n=0;n<nq;n++){
            auto q=q_partials(rt.e.rows[n],g);const R*co=&cs[n*J];
            for(int i=0;i<J;i++)for(int k=0;k<=i;k++)B[i*J+k]+=q[0]*co[i]*co[k]/nq;
        }
        for(int i=0;i<J;i++)for(int j=0;j<i;j++)B[j*J+i]=B[i*J+j];
        const auto dense=factor(B,false);
        DirectionPoint cache;cache.point=point;
        cache.Q.assign(state.begin(),state.begin()+M);cache.L=std::move(rt.L);
        cache.chol.reserve(size_t(J)*(J+1)/2);
        for(int i=0;i<J;i++)for(int j=0;j<=i;j++)cache.chol.push_back(dense[i*J+j]);
        direction_points.push_back(std::move(cache));
        return out;
    }

    void build_direction_cache(const VFStage&s) {
        if(!direction_points.empty())throw std::runtime_error("cache already built");
        direction_points.reserve(size_t(4)*s.nsteps);
        auto&state=direction_final_state;state.resize(size);
        for(int i=0;i<size;i++)state[i]=R(s.initial42[i]);
        for(int k=0;k<s.nsteps;k++){
            const auto&step=s.steps[k];R h=R(step.h);
            auto a=direction_cache_rhs(state,step.point_a,step.x);
            auto v=state;for(int j=0;j<size;j++)v[j]=state[j]+h/R(2)*a[j];
            auto b=direction_cache_rhs(v,step.point_mid,step.x+step.h/2);
            v=state;for(int j=0;j<size;j++)v[j]=state[j]+h/R(2)*b[j];
            auto c=direction_cache_rhs(v,step.point_mid,step.x+step.h/2);
            v=state;for(int j=0;j<size;j++)v[j]=state[j]+h*c[j];
            auto d=direction_cache_rhs(v,step.point_end,step.x+step.h);
            for(int j=0;j<size;j++)state[j]+=h*(a[j]+R(2)*b[j]+R(2)*c[j]+d[j])/R(6);
        }
        for(R v:state)if(!std::isfinite(v))throw DomainError("nonfinite cached native state");
    }

    std::vector<R> cached_direction_rhs(const DirectionPoint&cache,const std::vector<R>&t,int b) {
        const auto&g=coeff[cache.point];
        // Reconstruct complete angular rows from the identical native Q/L.
        // This pays the original branch checks again, but no point-root solve.
        const auto e=evaluate(cache.L,cache.Q,g,false);
        std::vector<R>a(M),right(J*b,R(0)),dP(nq*b,R(0)),dPt(nq*b,R(0));
        std::vector<std::array<R,2>>fpartial(nq);std::vector<R>factors(nq);
        for(int j=0;j<M;j++){
            a[j]=g.pnum[j]/g.pden;
            for(int col=0;col<b;col++)right[(j+1)*b+col]=g.target*t[(M+j)*b+col];
        }
        for(int n=0;n<nq;n++){
            const R*co=&cs[n*J],*si=&sn[n*M];const auto&v=e.rows[n];
            auto q=q_partials(v,g);fpartial[n]=flux_partials(v,g);
            R u=g.w2*(R(2)*v.K+v.K*v.K+g.E*v.P*v.P);
            factors[n]=(v.K+u/(R(1)+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd);
            for(int col=0;col<b;col++){
                R dp=0,dpt=0;
                for(int j=0;j<M;j++){
                    dp+=a[j]*t[j*b+col]*si[j];
                    dpt+=frequency[j]*a[j]*t[j*b+col]*co[j+1];
                }
                dP[n*b+col]=dp;dPt[n*b+col]=dpt;
                R chain=q[1]*dp+q[2]*dpt;
                for(int i=0;i<J;i++)right[i*b+col]-=chain*co[i]/nq;
            }
        }
        auto dL=right;
        const auto ix=[](int i,int j)->size_t{return size_t(i)*(i+1)/2+j;};
        for(int i=0;i<J;i++)for(int col=0;col<b;col++){
            R v=dL[i*b+col];for(int k=0;k<i;k++)v-=cache.chol[ix(i,k)]*dL[k*b+col];
            dL[i*b+col]=v/cache.chol[ix(i,i)];
        }
        for(int i=J-1;i>=0;i--)for(int col=0;col<b;col++){
            R v=dL[i*b+col];for(int k=i+1;k<J;k++)v-=cache.chol[ix(k,i)]*dL[k*b+col];
            dL[i*b+col]=v/cache.chol[ix(i,i)];
        }
        std::vector<R>dN(M*b,R(0));
        for(int n=0;n<nq;n++){
            const R*co=&cs[n*J],*si=&sn[n*M];const auto&v=e.rows[n];
            for(int col=0;col<b;col++){
                R dLv=dL[col],dU=0;
                for(int j=0;j<M;j++){
                    int m=frequency[j];R lj=dL[(j+1)*b+col];
                    dLv+=lj*co[j+1];
                    dU+=(-m*lj+(m*m-1)*a[j]*t[j*b+col])*si[j];
                }
                R dK=dLv-dPt[n*b+col];
                R df=dU*factors[n]+v.U*(fpartial[n][0]*dK+fpartial[n][1]*dP[n*b+col]);
                for(int j=0;j<M;j++)dN[j*b+col]+=df*si[j]/nq;
            }
        }
        std::vector<R>out(size*b,R(0));
        for(int j=0;j<M;j++)for(int col=0;col<b;col++){
            int m=frequency[j];R lj=dL[(j+1)*b+col];
            out[j*b+col]=g.sigma*((m*m-4)*t[j*b+col]+g.qlnum*lj/g.r3);
            out[(M+j)*b+col]=R(4)*g.sigma*t[(M+j)*b+col]+
                g.pref*m*(-m*lj+(m*m-1)*a[j]*t[j*b+col]+dN[j*b+col]);
        }
        for(int col=0;col<b;col++)out[K*b+col]=g.mean*dL[col];
        return out;
    }

    std::vector<R> apply_direction_cache(const VFStage&s,int b,const double*directions) {
        if(b<1||b>K||!directions||direction_points.size()!=size_t(4)*s.nsteps)
            throw std::runtime_error("complete cache/direction dimensions required");
        std::vector<R>t(size*b,R(0));
        for(int j=0;j<K*b;j++){
            if(!std::isfinite(directions[j]))throw std::runtime_error("nonfinite direction");
            t[j]=R(directions[j]);
        }
        size_t cursor=0;
        for(int k=0;k<s.nsteps;k++){
            const auto&step=s.steps[k];R h=R(step.h);
            if(direction_points[cursor].point!=step.point_a||direction_points[cursor+1].point!=step.point_mid||
               direction_points[cursor+2].point!=step.point_mid||direction_points[cursor+3].point!=step.point_end)
                throw std::runtime_error("cached frozen RK point order changed");
            auto a=cached_direction_rhs(direction_points[cursor++],t,b);
            auto v=t;for(size_t j=0;j<t.size();j++)v[j]=t[j]+h/R(2)*a[j];
            auto bb=cached_direction_rhs(direction_points[cursor++],v,b);
            v=t;for(size_t j=0;j<t.size();j++)v[j]=t[j]+h/R(2)*bb[j];
            auto c=cached_direction_rhs(direction_points[cursor++],v,b);
            v=t;for(size_t j=0;j<t.size();j++)v[j]=t[j]+h*c[j];
            auto d=cached_direction_rhs(direction_points[cursor++],v,b);
            for(size_t j=0;j<t.size();j++)t[j]+=h*(a[j]+R(2)*bb[j]+R(2)*c[j]+d[j])/R(6);
        }
        for(R v:t)if(!std::isfinite(v))throw LiteralJacobianError("nonfinite cached native JVP");
        return t;
    }

    size_t direction_payload_bytes() const {
        size_t n=direction_final_state.size();
        for(const auto&p:direction_points)n+=p.Q.size()+p.L.size()+p.chol.size();
        return n*sizeof(R);
    }
