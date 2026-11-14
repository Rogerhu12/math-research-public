# R215 重建：正 Hecke 卷积去掉 CM 谱及辅助素数平方代价

日期：2026-11-13。

**状态：已证明。** 本文对 R213 的实际在 $p$ 分歧环面角色，在一个未分歧辅助素数 $q$ 插入正卷积。它杀死阶四类型的全部 CM 谱，并给包含变化二次域与变化导子的完全显式误差。几何代价为 $q^2$，另保留准确的除数函数 $\mathcal T(q^2M)$。

## 1. 对象和主定理

保留 R213 全部设置，但现在参数 $\theta$ 的阶为四。因 $4\mid(p+1)/3$，有 $p\equiv3\pmod4$。令

$$F_p=\mathbb Q(\sqrt{-p}).$$

R181 说明 $\mathcal F_\theta(p^2)$ 中任何 CM 新形式的 CM 域都只能是 $F_p$。令 $\Omega=\Xi^{-1}$、$a$ 为其准确 prime-to-$p$ 环类导子，并记

$$M=Da^2,\quad h=h(\mathcal O_a),\quad
a_D=\prod_{\ell\mid D}\ell^{v_\ell(a)}\mid36,\quad a_0=a/a_D,$$

$$\mathcal L_a=\prod_{\ell\mid a}(1-\chi_K(\ell)/\ell)^{-1},\qquad
\mathcal T(X)=\max_{1\le m<X}\tau(m).$$

选择任意奇素数 $q$，满足

$$\boxed{q\nmid pDa,\qquad\chi_{-p}(q)=-1.} \tag{215.1}$$

不要求 $q$ 在正规化子二次域 $K$ 的分裂符号固定。

**定理 215.1。** 若

$$\boxed{
p>\frac{q+9}{q-1}\,
\frac{q^2a_D^2\,4^{\omega(D)}16^{\omega(a_0)}\mathcal T(q^2M)^2M}
{h\mathcal L_a^2},
} \tag{215.2}$$

则存在 **非 CM** 的 $f\in\mathcal F_\theta(p^2)$，使

$$a_q(f)\ne0,\qquad L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0. \tag{215.3}$$

此外有不需要任何除数函数的稳定充分条件

$$\boxed{p\ge q^2M\quad\Longrightarrow\quad(215.3).} \tag{215.4}$$

**定理 215.2。** 若还满足 $q\le M$，则对每个 $\epsilon>0$ 有完全有效、与 $K,a,p,q$ 无关的 $C_\epsilon^{\rm H}$，使

$$\boxed{p\ge C_\epsilon^{\rm H}q^2M^{1+\epsilon}/h
\quad\Longrightarrow\quad(215.3).} \tag{215.5}$$

一个可用选择为

$$C_\epsilon^{\rm H}
=15552X_{\epsilon/4}T_{\epsilon/12}^{2}\beta_{\epsilon/4}^{-2}, \tag{215.6}$$

其中有限乘积 $X_u,T_u,\beta_u$ 与 R87、R213 相同。定理不从“非 CM 子空间非空”推出其中有非零中心值；正卷积和几何主项是此处新增的必要步骤。

## 2. 正卷积的准确归一化

在 $G_q=\mathrm{PGL}_2(\mathbb Q_q)$ 中取 $U_q=\mathrm{PGL}_2(\mathbb Z_q)$，并定义

$$h_j=1_{U_q\operatorname{diag}(q^j,1)U_q}\qquad(j\ge0).$$

先按 $\operatorname{vol}(U_q)=1$ 作卷积。Bruhat–Tits 树的邻接路径计数给

$$\boxed{h_1^**h_1=h_1*h_1=h_2+(q+1)h_0.} \tag{215.7}$$

证明是：一个顶点的长度二返回路径恰有 $q+1$ 条；到任一距离二顶点的路径唯一；不存在到其他距离的长度二路径。$h_1$ 自伴，因为其逆双陪集在 $\mathrm{PGL}_2$ 中相同。

记右侧为 $H_q$。若使用 Pi 的局部 Haar 测度，$V_q=\operatorname{vol}(U_q)$，则

$$H_q=V_q^{-1}(h_1^**h_1)$$

仍是正卷积。作为**函数**，它始终准确为 $h_2+(q+1)h_0$；下文的轨道积分继续使用 Pi 的原测度。这里没有把球面双陪集 $h_2$ 和经典的 $T_{q^2}$ 混同：经典关系 $T_q^2=T_{q^2}+q$ 与 (215.7) 的单位项相差一，正是经典 $T_{q^2}$ 含有额外中心陪集的缘故。

把 R213 的测试函数在 $q$ 处的 $h_0$ 换成 $H_q$，其余各处不变，记所得全局函数为 $f^{(q)}$。

对一个未分歧自守表示，$h_1$ 在球面直线上的特征值按 $\operatorname{vol}(U_q)=1$ 的标准权二归一化为 $a_q(f)$。所以把 $h_0$ 换成 $H_q$，谱项准确乘上 $|a_q(f)|^2$。这也可以直接由球面直线上的正算子 $\pi(h_1)^*\pi(h_1)$ 得到，不依赖特征值符号。

因此 R213 的谱端变成

$$\boxed{
J(f^{(q)})=\frac{2\mathcal L_a^2}{pa\sqrt D}
\sum_{g\in\mathcal F_\theta(p^2)}
|a_q(g)|^2
\frac{L(\tfrac12,\pi_{g,K}\otimes\Omega)}{L(1,\pi_g,\operatorname{Ad})}.
} \tag{215.8}$$

局部 $p$ 处仍为 R213 的正则深度零矩阵系数，因此一维谱及其他类型仍被杀死。$q$ 在 $F_p$ 惰性，故每个 $F_p$-CM 新形式有 $a_q=0$；这是 CM 诱导表示在二次群外陪集的迹为零。因此 (215.8) 中全部 CM 项严格为零。一旦证明 $J(f^{(q)})>0$，就得到 (215.3)。

## 3. Singular 主项在两种 $K_q$ 中均有正下界

因为 $q\nmid Da$，$K_q$ 未分歧且 $\Omega_q$ 在单位上平凡。

若 $K_q/\mathbb Q_q$ 惰性不分歧，整个商环面 $T_q$ 位于 $U_q$，体积为一，且 $\Omega_q=1$。因此

$$I_q(0,H_q)=q+1.$$ 

若 $K_q\simeq\mathbb Q_q\times\mathbb Q_q$，可使环面成为对角环面，写

$$\Omega_q(x,y)=\chi(x/y),\qquad z=\chi(q),\qquad |z|=1.$$

商环面的每个赋值陪集体积为一。$h_0$ 只见赋值零，$h_2$ 只见赋值 $2,-2$，故

$$I_q(0,H_q)=q+1+z^2+z^{-2}\ge q-1.$$

记这个实数为 $A_q$。在两种情况下

$$\boxed{A_q\ge q-1>0.} \tag{215.9}$$

这也是 Feigon–Whitehouse Lemmas 4.4、4.6 的当前专门化。R213 的所有其他 singular 因子保持不变，$\Omega^2\ne1$ 仍消去第二个 singular 轨道，所以

$$\boxed{I_{\rm irreg}(f^{(q)})=A_q\frac{4h\mathcal L_a^2}{M}
\ge(q-1)\frac{4h\mathcal L_a^2}{M}.} \tag{215.10}$$

## 4. Regular 参数的区间只增加 $q^2$

FW Lemma 4.11 对双陪集 $h_j$ 的支集条件是在原判别式与导子指数之外额外允许 $j$。当前 $H_q$ 只含 $j=0,2$，所以结合 R213 的 $p$ 处条件，所有可能贡献的参数满足

$$\xi<0,\qquad v_p(\xi)\ge1,\qquad\frac{q^2M}{1-\xi}\in\mathbb Z.$$

置 $M'=q^2M$。与 R213 相同，允许参数包含在

$$\boxed{\xi_y=\frac{y}{y-M'},\qquad0<y<M',\qquad p\mid y.} \tag{215.11}$$

其中实际全局范数条件只会删去若干整数。如果 $p\ge M'$，区间内没有正的 $p$ 倍数，regular 部分为零。结合 (215.10) 已证明 (215.4)。

## 5. 辅助处的完整赋值计数

关键是不能把 $H_q$ 的双陪集体积 $\asymp q^2$ 额外再乘进误差。轨道积分只沿两个环面，直接计数得到更小的上界。

### 5.1 不分裂未分歧情形

此时 $T_q$ 紧且体积一，$|H_q|\le q+1$，故立即有

$$|I_q(\xi,H_q)|\le q+1. \tag{215.12}$$

### 5.2 分裂情形

在对角环面模型中，乘以固定环面元素最多改变一个模长为一的角色因子。因此计算绝对值时可取 regular 代表

$$\gamma_\xi=\begin{pmatrix}1&\xi\\1&1\end{pmatrix}.$$

两个商环面变量写成 $\operatorname{diag}(u,1)$、$\operatorname{diag}(v,1)$，得到

$$\begin{pmatrix}uv&u\xi\\v&1\end{pmatrix}.$$

置

$$m=v_q(u),\quad n=v_q(v),\quad s=v_q(\xi),\quad k=v_q(1-\xi).$$

矩阵的 Cartan 距离为

$$d=m+n+k-2\min(m+n,m+s,n,0). \tag{215.13}$$

每个整数赋值对 $(m,n)$ 的单位部分体积为一；$H_q$ 的值只取决于这些赋值。所以若 $N_j(s,k)$ 是 (215.13) 等于 $j$ 的整数对数目，则

$$|I_q(\xi,H_q)|\le N_2(s,k)+(q+1)N_0(s,k). \tag{215.14}$$

下面完整求出所需的计数。令 $\ell=\min(m+n,m+s,n,0)$。在 $d=j$ 下，

$$m+n=2\ell+j-k,$$

且恰有

$$k-j\le\ell\le0,\qquad
\ell-s\le m\le\ell+j-k. \tag{215.15}$$

最小值必须真正达到 $\ell$：若 $\ell$ 既不是端点 $k-j$ 也不是端点零，那么 $m$ 必须等于右式区间的某个端点。两个端点的 $\ell$ 则允许整个 $m$ 区间。

又有局部赋值的三种恒等关系：$k>0\Rightarrow s=0$；$k=0\Rightarrow s\ge0$；$k<0\Rightarrow s=k$。据 (215.15) 得到表：

| 赋值条件 | $N_0$ | $N_2$ |
|---|---:|---:|
| $k>2$ | $0$ | $0$ |
| $k=2$ | $0$ | $1$ |
| $k=1$ | $0$ | $4$ |
| $k=0$, $s\ge0$ | $s+1$ | $2s+8$ |
| $k<0$, $s=k$ | $|s|+1$ | $2|s|+8$ |

例如 $k\le0,j=2$ 时，两个端点 $\ell$ 各贡献区间内的全部 $m$，其余 $\ell$ 各贡献两个端点；$j=0,k<0$ 时区间只有一个 $m$，不能重复计算成两个。这分别给表中最后两行。

因此在 $k\le0$ 时，(215.14) 的右侧恰为

$$2|s|+8+(q+1)(|s|+1)
=(q+3)|s|+q+9\le(q+9)(|s|+1).$$

当 $k=1,2$ 时同一上界也成立。结合不分裂情形，全部未分歧 $K_q$ 都满足

$$\boxed{|I_q(\xi,H_q)|\le(q+9)(1+|v_q(\xi)|).} \tag{215.16}$$

对 (215.11) 的整数 $y$，记 $r=v_q(y)$、$t=v_q(M'-y)$。则 $v_q(\xi)=r-t$，故

$$|I_q(\xi_y,H_q)|\le(q+9)(r+1)(t+1). \tag{215.17}$$

这里角色相位只在取绝对值时舍去；没有假定分裂处的全局角色在一致化元上平凡。

## 6. 全球误差和主项比较

对 $\ell\mid a_0$ 仍取 R213 的

$$j_\ell=\min(v_\ell(y),2v_\ell(a)),\qquad B_\ell(j_\ell).$$

因辅助 $q$ 不除 $Da$，这些处的 $v_\ell(M')$ 与 $v_\ell(M)$ 相同；R213 的局部界可原样使用。其余普通素数与 (215.17) 的额外因子合在**一份** $\tau(y)\tau(M'-y)$ 中，不重复计算同一素数。得到

$$|I(\xi_y,f^{(q)})|\le
\frac{4(q+9)4^{\omega(D)}}D
\tau(y)\tau(M'-y)\prod_{\ell\mid a_0}B_\ell(j_\ell).$$

固定全部 $j_\ell$ 后，允许 $y$ 都是 $p\prod\ell^{j_\ell}$ 的正整数倍，个数至多 $M'/(p\prod\ell^{j_\ell})$。采用 R213 中已经完整证明的

$$\sum_{j=0}^{2n}\ell^{-j}B_\ell(j)<16\ell^{-2n},$$

便得

$$\boxed{|I_{\rm reg}(f^{(q)})|\le
\frac{4(q+9)q^2a_D^2\,4^{\omega(D)}16^{\omega(a_0)}\mathcal T(q^2M)^2}{p}.} \tag{215.18}$$

由 (215.2)，此值严格小于 (215.10)，所以 $J(f^{(q)})>0$。式 (215.8) 的所有 CM 项为零，故至少有一个非 CM 新形式同时满足 $a_q\ne0$ 和中心值非零。与 R213 一样，基变换的 Galois 不变性把 $\Omega=\Xi^{-1}$ 换回实际字符 $\Xi$。定理 215.1 得证。

## 7. $q\le M$ 时的完全有效统一常数

因为 $q\ge3$，

$$\frac{q+9}{q-1}\le6.$$

假定 $q\le M$，则 $q^2M\le M^3$。使用 R87 的有限乘积，

$$\mathcal T(q^2M)^2\le T_{\epsilon/12}^2(q^2M)^{\epsilon/6}
\le T_{\epsilon/12}^2M^{\epsilon/2},$$

$$4^{\omega(D)}16^{\omega(a_0)}\le X_{\epsilon/4}M^{\epsilon/4},$$

$$\mathcal L_a^{-2}\le\beta_{\epsilon/4}^{-2}a^{\epsilon/2}
\le\beta_{\epsilon/4}^{-2}M^{\epsilon/4}.$$

再用 $a_D^2\le1296$，(215.2) 的右侧至多为

$$7776X_{\epsilon/4}T_{\epsilon/12}^2\beta_{\epsilon/4}^{-2}
q^2M^{1+\epsilon}/h.$$

加一因子二保证严格不等式，即得 (215.6)。这证明定理 215.2。

若不假定 $q\le M$，保留 (215.2) 的明确算术判据即可；或者同样估计给

$$p\ge15552X_{\epsilon/4}T_{\epsilon/8}^2\beta_{\epsilon/2}^{-2}
q^{2+\epsilon/2}M^{1+\epsilon}/h$$

这一稍弱但对任意辅助 $q$ 都有效的充分条件。没有把 $\mathcal T(q^2M)$ 的 $q$ 依赖偷藏进绝对常数。

## 8. 与小非剩余选择的接口和剩余边界

R217 可在 $M\le p^A$ 时选取满足 (215.1) 且

$$q\le p^{1/(4\sqrt e)+\delta}$$

的素数。选 $\delta$ 足够小使 $3(1/(4\sqrt e)+\delta)<1$。若该 $q>M$，则

$$q^2M<q^3\le p^{3/(4\sqrt e)+3\delta}<p,$$

所以直接使用稳定范围 (215.4)。若 $q\le M$，使用定理 215.2。因而前述 $q\le M$ 条件并不破坏 R217 的 $\beta_2=1/(2-1/\sqrt e)$ 指数接口。

本结果填上阶四类型中心非消失可能全部来自 CM 的缺口；它仍只在明确的 $D,a,p,q$ 范围内给非消失。它没有给实际共同导子或二次判别式上界，也不排除整 $j$ 的异常曲线。

## 来源和独立证明的部分

- R213：实际深度零 $p$ 处矩阵系数、正谱端、主项、导子归一化与整数倍计数。本篇只在额外未分歧素数改变球面测试函数。
- B. Feigon, D. Whitehouse, *Averages of central L-values of Hilbert modular forms with an application to subconvexity*, **Duke Math. J. 149** (2009), 347–410，[作者全文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[DOI](https://doi.org/10.1215/00127094-2009-041)。Lemmas 4.4、4.6 给一般球面测试的 singular 轨道；Lemma 4.11 给双陪集支集。本文 §3 再直接计算所需 singular 因子；§5 对所需 regular 轨道给独立的完整赋值计数。
- R181：水平 $p^2$、平凡中心角色的阶四 CM 边界；CM 诱导表示在惰性素数的迹为零。
- R214：变化共同导子、中心平凡性及 $a_D\mid36$。
