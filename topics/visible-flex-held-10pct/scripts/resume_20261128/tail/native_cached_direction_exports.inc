// Independent handles own the original frozen config/stage bytes. A handle
// cannot be retargeted to another state; recreate it for every nonlinear state.
namespace vf_cached {
struct Handle {
    VFConfig config{};VFStage stage{};VFCallbacks callbacks{};
    std::vector<double>cosine,sine,halves,coefficients,initial;
    std::vector<VFStep>steps;
    std::unique_ptr<vf::Engine<long double>>engine;
    Handle(const VFConfig&c,const VFStage&s):config(c),stage(s),
        cosine(c.cosine,c.cosine+size_t(c.nq)*(c.M+1)),
        sine(c.sine,c.sine+size_t(c.nq)*c.M),halves(c.halves,c.halves+c.n_halves),
        coefficients(s.coefficients,s.coefficients+size_t(s.npoints)*(c.M+12)),
        initial(s.initial42,s.initial42+2*c.M+2),steps(s.steps,s.steps+s.nsteps) {
        config.cosine=cosine.data();config.sine=sine.data();config.halves=halves.data();
        stage.coefficients=coefficients.data();stage.initial42=initial.data();stage.steps=steps.data();
        engine=std::make_unique<vf::Engine<long double>>(config,stage,callbacks);
    }
};
void error_text(char*out,size_t cap,const std::exception&e){
    if(out&&cap){size_t n=std::min(cap-1,std::strlen(e.what()));std::memcpy(out,e.what(),n);out[n]=0;}
}
}
extern "C" int vf_cached_stage_create(const VFConfig*c,const VFStage*s,
    double*out,VFDiagnostics*d,void**handle,char*error,size_t cap) {
    if(handle)*handle=nullptr;if(d)std::memset(d,0,sizeof(*d));
    try {
        if(!c||!s||!out||!d||!handle)throw std::runtime_error("missing cache-create pointer");
        VFCallbacks empty{};vf::validate(*c,*s,1,1,empty);
        auto h=std::make_unique<vf_cached::Handle>(*c,*s);
        const auto begin=std::chrono::steady_clock::now();
        h->engine->build_direction_cache(h->stage);h->engine->diagnostics(*d);
        d->kernel_seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
        for(size_t j=0;j<h->engine->direction_final_state.size();j++){
            out[j]=double(h->engine->direction_final_state[j]);
            if(!std::isfinite(out[j]))throw vf::DomainError("nonfinite cached binary64 state");
        }
        *handle=h.release();if(error&&cap)error[0]=0;return 0;
    } catch(const std::exception&e){vf_cached::error_text(error,cap,e);return 1;}
}
extern "C" int vf_cached_stage_apply(void*handle,int columns,const double*directions,
    double*out,unsigned char*native_out,VFDiagnostics*d,char*error,size_t cap) {
    if(d)std::memset(d,0,sizeof(*d));
    try {
        if(!handle||!directions||!out||!d)throw std::runtime_error("missing cache-apply pointer");
        auto&h=*static_cast<vf_cached::Handle*>(handle);
        // All original runtime/grid/config guards remain in force on reuse.
        vf::validate(h.config,h.stage,1,1,h.callbacks);
        const auto begin=std::chrono::steady_clock::now();
        auto value=h.engine->apply_direction_cache(h.stage,columns,directions);
        h.engine->diagnostics(*d);
        d->kernel_seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
        for(size_t j=0;j<value.size();j++){
            out[j]=double(value[j]);if(!std::isfinite(out[j]))throw vf::LiteralJacobianError("nonfinite cached binary64 JVP");
        }
        vf::canonical(value.data(),value.size(),native_out);
        if(error&&cap)error[0]=0;return 0;
    } catch(const std::exception&e){vf_cached::error_text(error,cap,e);return 1;}
}
extern "C" size_t vf_cached_stage_payload_bytes(void*handle) {
    return handle?static_cast<vf_cached::Handle*>(handle)->engine->direction_payload_bytes():0;
}
extern "C" void vf_cached_stage_destroy(void*handle) {delete static_cast<vf_cached::Handle*>(handle);}
