# R133 补篇：精确径向参考相减、完整已知矩与同源 affine 数值合同

2026-11-15，visible-exact / tail_connector。

**准确恒等式与待执行的有限数值合同。** 本篇只为已经发布的
[SA](R133-supplement-signed-physical-cap-affine-and-complete-adjoint-receivers.md)
增加一个新已知 signed functional 的完整计算方法。SA 的最终身份是
blob f7db2f18230e62d216f8a901b990bfd9e6d703c0，
23,561 B，SHA256
85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1。
本篇不改其未知 $y$、原 formal/field/endpoint Grams、帽参数域或误差公式。

下述算术尚未执行。原 QR、实际 7908 行 coefficient/Gram、
RW、Green、F、CP 和所有成功科学消费者只读原件，不重新计算。

## 1. 同一个真实径向参考

固定原 $\eta_0$、修补中心 ac1/440866、真实物理帽
$I=[L,R]=[9/10,25/8]$。当前内禀参数变化的 bump 支撑不交 $I$；
这里的 $K,\beta,\gamma_{\rm rad},s$ 始终来自同一原 intrinsic/profile。

写已知修补 moving 中心为
$$
 \widehat Q=(u,v),\qquad v=s+\eta,\qquad
 m=\langle v\rangle_\phi=s+e,\qquad e=\langle\eta\rangle_\phi,
 \qquad \psi=I_\phi(v-m)/m,\qquad \Theta=\phi+\psi .
 \tag{SC.1}
$$
此处 $\eta$ 是完整已知扰动函数，不是固定内禀参数 $\eta_0$。
$u,\eta$ 的 quarter 标签支撑均不超过 32；物理角频率为 $4j$。
它们包括原 $\alpha$ **一次**和全部 exact continuous piece offsets。
$m$ 是完整 moving mean，未由 $s$ 或原 mean-completed response 替换。
归一角测度满足 $d\theta=(v/m)\,d\phi$。

原 [完整 scalar mean Green](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md)
Q.3（blob c7454ac2da81690f63ae3a1bbd9aa41643bc0a05，
10,843 B，SHA256 ebcd414e2fb14b5d598355465c615e91ab2b65214c802d78d5668692fe3c7bc3）
给的是精确旋转参考
$$
 s'= \beta s(1-Ks^2),\qquad C_{\rm ref}=1/s.
 \tag{SC.2}
$$
所以在与 SA 相同的物理方程
$$
 {\cal F}_{\rm phys}(B,C)
  =\big(\gamma_{\rm rad}A_\theta-2\beta B,\,
          \gamma_{\rm rad}B_\theta+\beta(A-C)\big),
 \qquad A=(K+B^2)/C ,
$$
中，
$$
 W_{\rm ref}=(0,1/s),\quad A_{\rm ref}=Ks,\qquad
 (W_{\rm ref})_r={\cal F}_{\rm phys}(W_{\rm ref}).
 \tag{SC.3}
$$
第二行由 $(1/s)'=\beta(Ks-1/s)$ 得到。第一行的角导为零。
这里只对精确 $s$ 使用 (SC.2)；有限中心的 $m'$ 仍是其真实保存导数。

令 $\widehat W=\Psi(\widehat Q)$，$U=\widehat W-W_{\rm ref}$。
于是准确地
$$
 R_{\rm phys}
 =U_r-\big({\cal F}_{\rm phys}(\widehat W)
                       -{\cal F}_{\rm phys}(W_{\rm ref})\big).
 \tag{SC.4}
$$
这没有改变 $R_{\rm phys}=D\Psi(\widehat Q)R_{\rm raw}$；
也没有把未知 $y=W_*-\widehat W$ 改成 $W_*-W_{\rm ref}$。
SA 的 $D_0$ 仍是对 $\widehat W$ 线性化的物理算子。

## 2. 分片积分中的全部端项

保留原 128 odd、128 even 加完整 even mean 的物理伴随
$z_\lambda=(z_{\lambda,B},z_{\lambda,C})$，输入
$\lambda=(\lambda_1,\ldots,\lambda_{96},a_\lambda)\in\mathbb R^{97}$
采用原正交基。对任意实际分片、右值减左值 $[z]_\tau$，
分片积分分部给
$$
 \int_L^R\langle z_\lambda,R_{\rm phys}\rangle_\theta\,dr
 =[\langle z_\lambda,U\rangle_\theta]_L^R
  -\sum_\tau\langle[z_\lambda]_\tau,U(\tau)\rangle_\theta
  +\int_L^R{\cal G}_\lambda\,dr ,
 \tag{SC.5}
$$
其中
$$
 {\cal G}_\lambda
 =-\langle(z_\lambda)_r,U\rangle_\theta
  -\langle z_\lambda,
       {\cal F}_{\rm phys}(\widehat W)
                  -{\cal F}_{\rm phys}(W_{\rm ref})\rangle_\theta .
 \tag{SC.6}
$$
$(z_\lambda)_r$ 是固定物理角的导数，再拉回 $\Theta$；
不是 $(z_\lambda\circ\Theta)_r$。因此下式没有漏掉或额外加入
$\Theta_r,m_r$。

原精确 shared-node Hermite 试件若按完整 receipts 验证连续，
则 $\sum_\tau[z]_\tau U(\tau)=0$ 是实际定义的结论。
不能仅由文件名或 proposal 的 finite-action check 宣告该项为零。
真 $L=9/10$ 使用首 Hermite 片的准确短延拓。
若任何侧值未通过精确共节点检查，全部实际跳项必须保留。

将 SA.30 的已知左项合并，得到同一个
$\widetilde{\mathcal B}_{\lambda,\delta}^{\,f}$：
$$
 \begin{split}
 \widetilde{\mathcal B}_{\lambda,\delta}^{\,f}
  ={}&\langle z_\lambda(R),U(R)\rangle
       -\langle z_\lambda(L),W_\delta(L)-W_{\rm ref}(L)\rangle\\
    &-\sum_\tau\langle[z_\lambda]_\tau,U(\tau)\rangle
       +\int_L^R{\cal G}_\lambda\,dr\\
    &-\langle Jz_{\lambda,B}(R),r_D^f\rangle
       -z_{\lambda,C,0}(R)r_m^f .
 \end{split}
 \tag{SC.7}
$$
这里 $W_\delta(L)=\Psi(Q_\delta(L))$，$Q_\delta=\widehat Q+\delta Z_{\rm can}$
只在已知 cut 值上使用，$|\delta|\le d=10^{-10}$。
因为 $U(L)+[W_\delta(L)-\widehat W(L)]
=W_\delta(L)-W_{\rm ref}(L)$，左端的中心项准确合并。
这一步同时改了已知积分和其两端；不能只改体 integrand 而沿用旧端项。

## 3. 只用 forward angle 的三组中心矩

对 $1\le l\le128$、$n_l=4l$ 定义
$$
 \begin{split}
 B_l&=\frac2m\langle u\sin(n_l\Theta)\rangle_\phi,\\
 C_l^c&=\frac2m\langle(1-v/s)\cos(n_l\Theta)\rangle_\phi
       =-\frac2{ms}\langle\eta\cos(n_l\Theta)\rangle_\phi,\\
 A_l^c&=\frac2m
    \langle(u^2+Kv^2-Ksv)\cos(n_l\Theta)\rangle_\phi\\
       &=\frac2m
    \langle\{u^2+K(s+\eta)\eta\}\cos(n_l\Theta)\rangle_\phi .
 \end{split}
 \tag{SC.8}
$$
这是 $B,\ C-C_{\rm ref},\ A-Ks$ 的完整物理 sine/cosine amplitudes。
例如
$\langle v\cos(n_l\Theta)\rangle_\phi
=m\langle\cos(n_l\theta)\rangle_\theta=0$；
所以非零模上将常量 $1$ 换成 $1-v/s$ 是准确等式，
不是删除某个真实 Fourier 项。

其物理 mean 必须独立保存：
$$
 B_0=0,\qquad
 C_0^c=-\frac{e}{ms},\qquad
 A_0^c=Ke+\frac{\mathcal V}{m},\qquad
 \mathcal V=\langle u^2\rangle_\phi
                  +K\langle(v-m)^2\rangle_\phi .
 \tag{SC.9}
$$
$B_0=0$ 仅用当前反射族；$C_0^c,A_0^c$ 不设零。
$\mathcal V$ 用完整 signed finite convolution 或等价 Parseval 公式；
本篇不把带 $K$ 的表达式在一般复/负曲率域称为正量。

若
$$
 z_B=\sum_{l=1}^{128}b_l\sin(n_l\theta),\qquad
 z_C=c_0+\sum_{l=1}^{128}c_l\cos(n_l\theta),
$$
则 (SC.6) 精确成为
$$
 \begin{split}
 {\cal G}_\lambda={}&\frac12\sum_{l=1}^{128}
 \big[
 (-b_l'+2\beta b_l-n_l\gamma_{\rm rad}c_l)B_l\\
 &\hspace{2.7em}
 +(-c_l'+\beta c_l)C_l^c
 +(n_l\gamma_{\rm rad}b_l-\beta c_l)A_l^c
 \big]\\
 &+(-c_0'+\beta c_0)C_0^c-\beta c_0A_0^c .
 \end{split}
 \tag{SC.10}
$$
边界配对为
$$
 \langle z,U\rangle
       =\frac12\sum_{l=1}^{128}(b_lB_l+c_lC_l^c)+c_0C_0^c .
 \tag{SC.11}
$$
所有 $b_l,c_l,c_0$ 都是原 97 个输入的完整行向量。
$1/2$ 来自归一圆上的 sine/cosine 正交性；
even mean 的权是 $1$，不乘 $\alpha$ 或 $1/\sqrt2$。
原试件 128 的物理支撑只限制已知测试函数，
不截断实际帽解、$\Theta$ 的指数级数或未知输出。

## 4. 一个完整径向矩引理

对实 $r,\phi$，令 $q,\psi$ 是已知 finite Fourier 函数，$\psi$ 为实值，
并令
$$
 M_l(q;r)=\left\langle q(r,\phi)
             e^{i n_l\phi}e^{i n_l\psi(r,\phi)}\right\rangle_\phi .
 \tag{SC.12}
$$
(SC.8) 分别取其虚部或实部，所需三个 $q$ 是
$2u/m$、$-2\eta/(ms)$、
$2\{u^2+K(s+\eta)\eta\}/m$。
$\beta,\gamma_{\rm rad}$ 为径向量，可先乘进 $q$，
再使用同一引理，避免把它们当常量移出真实径向积分。

以普通径向导数（不是除以阶乘的 Taylor coefficients）写
$$
 \begin{split}
 A_0&=q,\\
 A_1&=q_r+i n_l q\psi_r,\\
 A_2&=q_{rr}+2i n_lq_r\psi_r
           +i n_lq\psi_{rr}-n_l^2q\psi_r^2.
 \end{split}
 \tag{SC.13}
$$
则 $M_l^{(j)}=\langle A_j e^{i n_l\phi}e^{i n_l\psi}\rangle$，
$0\le j\le2$。这是先求导后的完整表达式，没有对数值 remainder 求导。

假设同一闭径向行上有
$$
 Q_k\ge\sup_r\|\partial_r^kq\|_{\mathcal A_0},\qquad
 P_k\ge\sup_r\|\partial_r^k\psi\|_{\mathcal A_0},
 \qquad 0\le k\le3 .
$$
由于在真实角上 $|e^{i n_l\psi}|=1$，有完整三阶界
$$
 \begin{split}
 |M_l'''|\le {\mathfrak T}_l(q):={}&
 Q_3+3n_lP_1Q_2
 +3(n_lP_2+n_l^2P_1^2)Q_1\\
 &+(n_lP_3+3n_l^2P_1P_2+n_l^3P_1^3)Q_0 .
 \end{split}
 \tag{SC.14}
$$
这里仅用 $\mathcal A_0\to L^\infty$ 和真实角平均，
没有声称 $e^{i n_l\psi}$ 的 Wiener norm 是 $1$。
若参数或角不是实值，不能复用 (SC.14) 的单位模论证；
须恢复相应完整指数 majorant。本合同的实际积分只在原真实 $\eta_0$、真实 $r$，
参数展开只在真实 $|\delta|\le d$ 上取余项。

## 5. 指数截断保留无限尾；有限 Fourier 部分无 alias

在一个已保存的实际 midpoint $c$，取完整有限多项式
$$
 E_P=\sum_{k=0}^P\frac{(i n_l\psi)^k}{k!},\qquad
 {\cal T}_{P,l}
 =\exp(n_lP_0)\frac{(n_lP_0)^{P+1}}{(P+1)!}.
 \tag{SC.15}
$$
Banach algebra 的 Taylor 余项给
$\|e^{i n_l\psi}-E_P\|_{\mathcal A_0}\le{\cal T}_{P,l}$。
因此将 (SC.13) 的第 $j$ 个积分用 $E_P$ 计算时，
完整误差至多
$$
                    \|A_j\|_{\mathcal A_0}{\cal T}_{P,l}.
 \tag{SC.16}
$$
数值函数只在这一步截取指数多项式；全部原 finite coefficients、mean
以及 (SC.16) 都保留。

有限 Fourier 系数可用完整卷积，或用有证明无 alias 的有限 DFT。
若 quarter 支撑上界为 $\deg q=D_q,\ \deg\psi=D_\psi$，
则 $\deg A_j\le D_q+jD_\psi$，所以准确读取所需第 $-l$ 系数的充分条件是
$$
              N>D_q+(P+j)D_\psi+l .
 \tag{SC.17}
$$
$N$ 是整个复 Fourier 数组长度，不是最高物理频率。
采用 DFT 时 roots of unity、矩阵算术和舍入必须由有向区间覆盖；
一个普通浮点 FFT 加尾项不是完整证书。

对于原 degree32 body 中心，$D_q\le64,D_\psi\le32$。
故 $P=32,N=2048$ 足以覆盖全部 $j\le2,l\le128$。
对于 selected degree96 cut，$D_q\le192,D_\psi\le96$；
$P=32,N=4096$ 同样满足 (SC.17)。
特别二阶参数导的 $A_2$ 可到 degree384，不能误写为 degree288。
这些是有限支撑的整数检查，不是实际误差小门；
实际 (SC.16) 仍必须完整计算并报告。

每个 midpoint 的三个矩共用于全部原 97 列。
实现可以对 $l$ 分批，但不得截断测试的 128 个物理模，
不得将同一 Fourier coefficient 的区间中心冒作其有向包围。

## 6. 只消费旧 scalar jets 的准确径向积分

原 7908 个完整闭行提供同一实际 midpoint 的 scalar jets 与 whole third jets。
每行必须核其 exact interval、actual_scalar_germ、原 candidate piece、
原 repair 身份及 canonical row SHA。这里使用一个明确的逐行门：
若原行是 $[\ell,h]$，以原 knot 表取
$p=\operatorname{bisect\_right}(\mathrm{knots},\ell)-1$，须有
$$
 \mathrm{knots}[p]\le\ell<h\le\mathrm{knots}[p+1],
 \qquad c=(\ell+h)/2 .
 \tag{SC.18a}
$$
因此整个原行及其中点都属于同一个 actual candidate cubic 和同一 repair offset。
原已成 core
fourfold_codazzi_cap_adjoint_residual_Gram_core.py 的
CachedCoefficientProvider.from_saved 已先做这一门，再分别以
同一个 $p$ 计算 wholejets 和 centjets；其 immutable blob 为
a7ff6a1f5bc11fa9bd81cf1eec95eba908310e71，
21,822 B，SHA256
689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc。
四个原 pilot 和其余 7904 行沿用这同一入口。
新 runner 必须再次按原数据逐 7908 行核 (SC.18a)，而非仅引用旧计数。

若这个门失败，本合同不允许用另一 candidate 片在旧 $c$ 的中心 jet；
本次新结论直接失败。它没有授予跨片延拓或新 intrinsic midpoint。
给定上述 $c$，(SC.13)–(SC.16) 得到
$M_l(c),M_l'(c),M_l''(c)$ 的完整有向球。
由 (SC.14)，在同闭行有
$$
 M_l(r)
 =M_l(c)+M_l'(c)(r-c)
          +\tfrac12M_l''(c)(r-c)^2+\epsilon_l(r),\qquad
 |\epsilon_l(r)|\le\tfrac16{\mathfrak T}_l(q)|r-c|^3 .
 \tag{SC.18}
$$

$r$ 的所有导数由同一原 jets 做有限加、乘、除法递推。
例如 $a=1/m$ 的普通导数满足
$$
 a_0m_0=1,\qquad
 a_k=-m_0^{-1}\sum_{i=1}^k {k\choose i}m_i a_{k-i},
 \qquad 1\le k\le3 .
 \tag{SC.19}
$$
对 $1/s$ 同理。每个 whole row 必须保原 $s,m$ 同符号、
严格非零的分母门；不能以 midpoint 的非零代替 whole row 门。
$u,\eta$ 的实际 cubic jets 与分片常 offset 由原 exact candidate/repair 给出。
(SC.9) 的两个 mean 用相同 scalar jet 递推，单独做 (SC.18)；
不从 nonmean 矩的零模猜取。

将原 Hermite partition、7908 scalar partition、candidate/repair 接片
取真实公共交集。对每个交段，原伴随 Hermite 是同一 exact cubic，
其 $r$ 导是 exact quadratic。
在 (SC.10) 中分别为未乘、乘 $\beta$、乘 $\gamma_{\rm rad}$ 的矩
建立 (SC.18)，随后与相应 $b_l,c_l,b_l',c_l'$ 做完整多项式乘积，
按真实 $dr$ 准确积分有限多项式。所有径向仿射换元保真实 Jacobian。

例如已知行向量多项式 $p(r)$ 乘某矩，其 remainder 行向量范数可收为
$$
 \frac{{\mathfrak T}_l(q)}6
            \int_{\rm cell}|r-c|^3\|p(r)\|_{\mathbb R^{97}}\,dr .
 \tag{SC.20}
$$
可用 exact polynomial coefficients 的完整正 majorant 对该积分作有理上界。
对同一个 $\lambda$ 的各模、各胞元和各类误差使用 triangle；
不能把不同来源当作正交误差平方相加。
若逐 97 分量保存有向区间，最后对同一个完整向量取 Euclidean norm，
其 component radii 的二范数是合法同时误差；不额外随意乘或省 $\sqrt{97}$。

将旧行 restrict 到真交段时，(SC.18) 的旧 Taylor 中心仍可保留，
不把 whole remainder 按交长比例缩小。
更细的径向求积只允许积分已知同一 Taylor 模型及其完整误差，
不能从旧固定 midpoint 免费制造新的精确 intrinsic midpoint jets。

## 7. 已知 selected cut 和左 target 的有限维费

在 $L$ 用原 directed complete raw193 cut amplitudes 和 canonical
continuous direction 的完整修补费构造 $Z_{\rm can}(L)$；
其支撑为 96，mean 槽完整，**不乘 $\alpha$**。
原 global pair $\mathcal A_0$ 修补费 $E_Z=2.292\,10^{-16}$
是同一 canonical direction 的分片常 offset，不是 completed-mean scalar flow。
若用逐系数 boxes 包围这项 joint 误差，允许较宽的完整 box；
实际使用的 box 放大须进入最终认证，不能再在末端重复加同一 offset。

可以在 $\delta=0$ 给 (SC.8)–(SC.11) 的 selected cut 配对做二阶参数展开，
并在完整实段 $|\delta|\le d$ 用 (SC.14) 的参数版本付三阶余项。
此处把 $r$ 换成 $\delta$，而 $s,K$ 固定；
$\partial_\delta^k m$、$\partial_\delta^k\psi$ 和各 reciprocal
按 (SC.19) 精确求得。分母和角图门均须对完整参数段验证。
所有指数尾、endpoint 算术和 direction 区间误差仍保留。
因此 SC.7 产生一组完整 signed 97-vector 的参数 Taylor 模型和明确余项，
而不是把参数上下端两次 norm 相减。

SA.31 的新左缺陷不要求重新计算旧 $E_{L,0}$ Gram。
令 $\mu=\langle Z_2(L)\rangle$、$M\ge|\mu|$，
$j_\delta=v_\delta/m_\delta$，并在同完整参数段有
$$
 0<j_-\le j_\delta\le j_+,\qquad |m_0|-dM>0,\qquad
 S_0\ge\|Z_2-\mu j_0\|_{\mathcal A_0}.
$$
$S_0,M$ 可直接读已成 cut 的 complete_shape_A0 与 complete mean，
不把 raw cut midpoint 当 directed enclosure。
准确地
$$
 \partial_\delta S_\delta^*f
  =\left[\mu f-j_\delta^{-1}
                   I(Z_2-\mu j_\delta)f_\phi\right]\circ\Phi_\delta,
 \qquad
 Z_2-\mu j_\delta
      ={m_0\over m_\delta}(Z_2-\mu j_0).
 \tag{SC.21}
$$
利用 $\|I\|_{\mathcal A_0\to L^\infty}\le1/4$、
$\|f_\phi\|_2\le384\|f\|_2$ 和
$d\theta=j_\delta\,d\phi$，得到
$$
 \begin{split}
 D_{\rm target}
 &=d\sqrt{j_+}
 \left[M+96j_-^{-1}
       {|m_0|\over |m_0|-dM}S_0\right],\\
 \|(S_\delta^*-S_0^*)P_{96}^{\rm odd}\|_{2\to2}
 &\le D_{\rm target},\qquad
 E_{L,\delta}\le E_{L,0}+D_{\rm target}.
 \end{split}
 \tag{SC.22}
$$
若 $m_0$ 只以区间给出，对分式使用其真实最大值；
不以错误的 upper 分母作下界。这里的 $|m_0|$ 可用同一固定值的
安全区间评价，或将比例宽为
$1+dM/(m_{0,-}-dM)$。
独立 scalar mean 测试 $a_\lambda$ 不随 $S_\delta$ 改变；
没有维数因子 $\sqrt{97}$。

## 8. 已成 Grams、真外端及未知修正仍各自收费

新 signed 积分只改变 SA.30 的计算方法。
SA.22/31 的真实误差仍为
$$
 \begin{split}
 {\cal E}_{\rm true}={}&
 (D_w+13\rho Q_w)Y_w
 +E_{L,\delta}Y_L^\delta
 +(E_R+L_DZ_B+L_mZ_m)Z_R\\
 &+\sum_\tau J_\tau\|y(\tau)\|.
 \end{split}
 \tag{SC.23}
$$
$\rho=3\,10^{-6}$，$y=W_*-\widehat W$，
$Y_L^\delta$ 是原 SA.31 的完整 selected 左差界。
始终保留原非零 affine 值，不能用只含 $\gamma$ 的响应代替 $Y_w,Y_L^\delta$。

最小版本可取 $w=1$，从原完整 formal ordinary Gram 和 field Grams
直接付 $D_1,Q_1$；$H_0$ 不重复收费。
若另作新的 weighted recombination，只能恢复原每个完整 cell 的 PSD Gram，
乘同胞元完整权上界后求和；不能由 whole Gram 作长度比例 restriction，
也不能拿一个 input-side Gram 的主块当作 output receiver。
本次三矩计算不产生新的未知修正小界。

对外端可选择精确 signed 值，或保完整缺项费。
若将 SC.7 最后两项暂以零为数值近似，必须加
$$
             {\cal E}_{\rm out,known}
                  =Z_B r_{D,+}+Z_m r_{m,+}.
 \tag{SC.24}
$$
当前修补中心须读
[A.15](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md)
的 $r_{D,+}=1.3\,10^{-15},\ r_{m,+}=2.05\,10^{-19}$，
及其原实际 $f$ 域。
不能把 A.13 未修补中心的更小数直接转给 440866。
$J^*J=1$ 只在 nonmean 上使用；$C$ mean 的第二项独立存在。
若这份外端界已对整个 $f$ 球统一，不能又重复加入同一 height 改变；
若只固定 $f_{\rm ref}$，其他 $f$ 仍按 SA.27 另付。

若 $\widehat b_\delta$ 是新 SC.7 signed 模型，其全部数值/截断误差为
$\mathcal E_{\rm num}$，则结论只是
$$
 \|b_\delta^f-\widehat b_\delta\|_{97}
       \le {\cal E}_{\rm num}
              +{\cal E}_{\rm out,known}+{\cal E}_{\rm true}.
 \tag{SC.25}
$$
其中 $\mathcal E_{\rm out,known}$ 仅在相应 signed 项未实际计算时使用。
实际 $b_\delta^f$ 仍是 SA/SR 的同一个完整 inner $B$ 加 $C$ mean 源。
低 trace、core 自映像、$H^1$ chart、waist 与 high body/cut 的入口
没有从 (SC.25) 自动得到。

## 9. 最小原件恢复与新科学执行边界

准备单 adc2f9fa905093e128b743ea77e78537a0063cfc，
26,732 B，SHA256
d2164acdd52633cbd7c3eebb4d54679e590ee3afc642aa5ddc7fc895fb3de1ac，
只是恢复元数据，不是可部署 manifest。实际 runner 必须逐一 pin：

1. 原 v2 完整 proposal inventory、原 7908 plan 和 32 个 exact original slice。
每 slice 的四个原 Hermite arrays、完整 quarter rows 逐 SHA 核验；
重合 shared nodes 必须逐 exact 值一致。
2. 四个原 pilot 请求 $(0,4,0),(16,4,0),(1024,4,0),(1976,4,3)$
不在原 64 reused quarters 内。它们只从原
$[0,256)$、$[1024,1280)$、$[1792,1977)$ 三个 successful ranges
恢复；再按原 7908 plan 的 canonical row SHA 核。
不能从原 pilot Gram 或 64-point native 猜出其 scalar jets。
3. 完整 ac1 五个 candidate shards、原 exact repair 定义和 offset-sequence hash、
原 directed cut193、base65 及 canonical direction 修补身份。
所有 native 文件只临时恢复；$\alpha$ 和真实 mean 单位必须检查。
4. 原 formal/field/endpoint signed Grams 和成功执行记录、RW 完整 affine
及同参数域的小结、已发布 SA 和本合同。原 producer 仅作为定义证据，
不调用其旧 target、QR、Gram、convolution 或积分入口。

全部 7908 原闭行都须覆盖真实 $[9/10,25/8]$；错误/缺失行使本次新结论失败。
所有 branch signs、128 物理模、97 输入和完整 mean 均保留。
新科学只包括 (SC.8)–(SC.25) 的 known moments、有限新产品/积分、
已成正误差的明确读出及参数模型，不重做成功数学。

完整逐行审计留在 Actions 临时目录并保存其 bytes/SHA。
持久小结保全部 97 signed coefficients、参数余项、
每类数值误差、独立 mean、原件身份/覆盖门、完整 (SC.23)–(SC.25)、
所有未通过门及实际 child status。
须先原子保存科学结果，再打印带 bytes/SHA 的可恢复小 payload，
然后才允许 Git publication；科学小结目标不超过 45 KB，
完整 prepublication payload 不超过 59 KB。
包装失败不把成功已保存的新科学重跑；输入域或科学失败如实记录。
本合同尚未宣称任何新增数值门通过。
