# R1040：原 p≡5 mod12 行的实际 Hodge graph 与本原 MW 消去

日期：2026-11-27（UTC+8；2026-11-26 16:00 UTC）。
会话：Astra-serre-24b8836b-20261126。
o1_theta / root；CM 自扭排除与核角色另经 global_route 核对。

**已证明：R1038 的原 p5 Raynaud 最低型具有实际整对称配对、
准确 Hodge graph 算子及本原整 MW 消去泛函。**
本篇重新支付双无穷尾的真实 Frobenius、算术下降及原 CM 角色，
再应用两次 PD 比较；不把 p11 的整个 Jacobian 好约化移到本行。

本原性适用于 \(p>C_*\)，其中 \(C_*\) 是 R1026 (1026.13)
固定的绝对整数。泛函消去原全部 Mordell–Weil 对数的饱和交；
它对 R1039 指定 CM jet 的值仍是一个须证明非零的准确有限读数。

## 1. 实际 good BT 与两次 PD 的整格

全篇设
\[
p=12g+5\ge41,\quad m=6g+2,\quad h=m/2=3g+1,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad \varepsilon=\pi_0^m.
\]
使用 R1038 同一个原 \(J_1\)、\(P=(p-1)D_0\)、Raynaud
\(0\to T\to G\to B\to0\) 和真实整 \(e_1\)。
该文已构造
\[
\mathcal G_1=e_1B[p^\infty]\simeq e_1G[p^\infty],
\]
其特殊晶体仅有惯性 \(\pm m\)，Hodge 纯为一格。
R1035 §§1–4 的 BT 引理只使用这些前提及
\(2m=p-1,e_0=m(p+1)\)，不依赖 \(p\bmod4\)。

具体地，在 \(R/(\varepsilon^2)=k[\pi_0]/(\pi_0^{p-1})\)
的短 PD 厚化上，graph 系数所需的 \(\pm2m\) 角色都不存在，
实际群因而为常数群。第二次在 \((\varepsilon^2)\) 上用
\(x^j/j!\) 的合法 topologically nilpotent PD 结构，
得到真实、态射相容的整比较
\[
M=M_H\oplus M_L,\qquad
\operatorname{Fil}=\{u+\Phi(u):u\in M_H\otimes R\},
\]
\[
\Phi(M_H)\subset\varepsilon^2(M_L\otimes R),\qquad
M_L\otimes R\simeq\operatorname{Lie}\mathcal G_1 .
\tag{1040.1}
\]
所有 factorial 估值与两个不同 PD 基变换图均按 R1035 已证引理使用，
不对 \((\pi_0)\subset R\) 作非法阶乘除法。

原 Jacobian 的 Raynaud abelian polarization 在特殊
\(B_k=\prod\operatorname{Jac}(D)\) 上是各正规化分量的 principal
polarization，故它本身为 principal。\(e_1\) 自伴，
所以在 \(\mathcal G_1\) 上的极化完美。协变约定保留
\[
\langle\omega_s,f_t\rangle=2\delta_{st},\qquad
\langle f_s,\omega_t\rangle=-2\delta_{st}.
\tag{1040.2}
\]
通过极化写成曲线 cohomology 时，真正 \(\delta_*\) 的协变作用
是 \((\delta^{-1})^*\)，不与自然曲线拉回混用。
原 split-Hecke、实际本地 \(T_5\)、deck 及算术下降均随 (1040.1) 运输。

## 2. 真正双无穷尾上的算术 Frobenius 平方

记 \(\alpha\) 为原算术下降：在 \(W(k)\) 上为 \(p\)-Frobenius，
并取 \(\alpha(\pi_0)=\pi_0\)。
它分别保持 \(M_H,M_L\)，与晶体 \(F\) 相容且交换；
\(F\) 因半线性而交换这两格。定义
\[
\Pi=F\alpha^{-1}.
\tag{1040.3}
\]

### 2.1 原 source framing 与六标记相位

R1038 的全部 SS 标记 \(s\in S\) 属于 \(\mathbf F_{p^2}\)。
对原 source 椭圆曲线的 \(\mathbf F_{p^2}\) 模型，
\(j\ne0,1728\) 时相对 Frobenius 与 Verschiebung 的比较给
\(\operatorname{Fr}_{p^2}=[\pm p]\)，因为自同构只有 \(\pm1\)。
原 \(s=0\) 的 \(j=0\) 模型定义于 \(\mathbf F_p\)；
立方双射给 trace 零，因此其平方为 \([-p]\)。
本行的 \(j=1728\) ordinary，不属于 \(S\)，故没有尚未处理的四次相位。

R1038 保留的 source/target 首项是
\[
C_s^{p-1}=U_{{\rm source},s}^{-1},\qquad
U_{{\rm source},s}=g_sk_s^p,\quad
U_{{\rm target},s}=k_sg_s^p.
\]
实际 source 参数在 \(\mathbf F_{p^2}\) 上的
\([p]\) 首项为 \(\pm1\)。
特殊形式群所有端同态亦在此域定义，因为算术平方以这个标量共轭它们；
所以原 \(\mu_{p^2-1}\) framing 与单位平均可在同一域进行。于是
\[
C_s^{p-1}=\pm1,\qquad C_s\in\mathbf F_{p^2},\qquad
A_s=-3C_s^2\in\mathbf F_p^\times .
\tag{1040.4}
\]
若 source 平方为 \(-p\)，则 \(-p\equiv1\bmod6\)，六标记无修正；
若为 \(+p\)，则 \(p\equiv-1\bmod6\)，修正为共同 \([-1]\)，
已被 \(N_{\rm ns}\) 中 \(-I\) 消去。
因此 \(\alpha^2\) 在原尾
\[
D_s:\quad Y^2=X(X^{(p+1)/2}+A_s)
\tag{1040.5}
\]
上没有遗漏的 deck 或四次扭曲；两个 \(\mathbf F_{p^2}\) 无穷点
也是这个真实模型的点。

### 2.2 Hermitian 来源不依赖次数奇偶

置 \(n=(p+1)/2\)。对任意 \(A\in\mathbf F_p^\times\)，
可取 \(a^n=A\) 于 \(\mathbf F_{p^2}\)。
其 norm 为 \(A^2\)，故 \(a\) 与 \(aA\) 均是该域的平方。
取 \(b^2=aA\)，\(X=aX_1,Y=bY_1\) 给 \(D_A\simeq D_1\)。

Hermitian 曲线
\(V^{p+1}=U^{p+1}+W^{p+1}\)
经 \(X=u^2,Y=u\,v^n\) 非恒定地映到 \(D_1\)。
任一几何点 \(Q\) 的切线交因子为
\(p[Q]+[\operatorname{Fr}_{p^2}Q]\)；
与一个 \(\mathbf F_{p^2}\) 点的切线相比，得到
\(\operatorname{Fr}_{p^2}=[-p]\) 于其 Jacobian。
这一纸面切线证明见 R1036 §3，完全不使用 \(n\) 偶。
Jacobian norm 满射将等式传到 \(D_1\)，再传到每个实际 \(D_s\)。

R1038 的最低 \(\pm m\) 晶体只来自这些尾；
中心、图及支持 CM 尾没有这两个角色。
结合 §2.1 的实际下降，有
\[
F^2=-p\,\alpha^2,\qquad
\boxed{\Pi^2=-p.}
\tag{1040.6}
\]
这是原模型上的等式，不从抽象 superspecial 类型推断符号。

## 3. 完美整配对与原双节点的准确常数

极化相容性给 \(\Pi^\dagger\Pi=p\)，故
\(\Pi^\dagger=-\Pi\)。
R1035 的整格引理给 \(F:M_L\to M_H\) 是单位同构，
因此
\[
B(v,w)=\langle\Pi v,w\rangle
\tag{1040.7}
\]
为整、对称、完美的双线性形式。
原 \(\delta=\delta_*\) 满足
\[
\Pi\delta=\delta^{-1}\Pi,\qquad
B(\delta v,w)=B(v,\delta w).
\]
所以 \(D=(\delta-\delta^{-1})/(\zeta-\zeta^2)\) 为 \(B\)-自伴。
这是外部整线性算子，不将其冒称 BT 端同态。

R1038 的两个 exact germs
\(\psi_+=\beta^{p-1},\psi_-=\alpha^{p-1}\) 满足同一个真实恒等式
\[
\psi_\pm^p=\mathcal D_s-C_s^{p-1}/\psi_\pm .
\]
两个 annular cochains 同时减去单个 affine regular
\(\mathcal D_s\)，所以真实 \(F(f_s)\) 由 \(d\mathcal D_s\) 表示。
在两无穷端，
\(\psi_\pm=\pm z^{-h}(1+\cdots)\)，
\(\omega_s=\mp z^{h-1}(1+\cdots)dz\)，故
\[
\boxed{\quad
\bar F(f_s)=-hC_s^{p-1}\omega_s
           =\frac{C_s^{p-1}}4\,\omega_s .
\quad}
\tag{1040.8}
\]
这里 \(h=(p-1)/4\)，两端给同一个比值；没有额外因子二。

设
\[
r=1-b^3,\quad A=A_p=bQ_p(b^3),\quad
d_A=\deg A=6g+1=(p-3)/2,\quad k_0=8g+2=(2p-4)/3,
\]
\[
e_s=\theta_sf_s,\qquad
q_s=C_s^{p-1}\theta_s^{p+1}
           =-\frac{r_s^{k_0}}{A'(s)^2}.
\tag{1040.9}
\]
原节点式 \(b-s=\varepsilon\theta_s\psi_s+\cdots\)
和 \(\alpha(\varepsilon)=\varepsilon\) 准确给
\(\alpha(e_s)=e_{s^p}\)，对整个双节点 pair 使用。
由 (1040.2)、(1040.8)，
\[
\bar B(e_s,e_t)=\frac{q_{s^p}}2\,{\bf1}_{t=s^p}.
\]
对称性及 (1040.9) 的 \(\mathbf F_p\) 来源再给
\[
\boxed{\quad
q_s=q_{s^p}=q_s^p\in\mathbf F_p^\times,\qquad
\bar B(e_s,e_t)=\frac{q_s}2\,{\bf1}_{t=s^p}.
\quad}
\tag{1040.10}
\]
这保留原 \(\theta_s\)、算术置换和 Serre 尺度。

## 4. 实际 Hodge graph 的矩阵与完整原首 log

定义由实际 Fil 给出的整 Lie 算子
\[
\mathcal Q=\varepsilon^{-2}\Phi\Pi.
\tag{1040.11}
\]
Fil 各向同性给 \(\mathcal Q\) 为 \(B\)-自伴；
它与原 split-Hecke 交换，并满足
\[
\mathcal Q\delta=\delta^{-1}\mathcal Q.
\]
因此 \(B(v,\mathcal QDw)\) 是整交错型且对 split-Hecke 平衡。

这个算子的模 \(\pi_0\) 必须由实际源计算。
在 \(R/pR\) 中，绝对 Frobenius 杀 \((\varepsilon^2)\)，
因而实际 \(\mathcal G_1^{(p)}\) 经第一次 PD 比较成为常数群。
第二次 PD 的态射自然性给真正相对 Verschiebung 的晶体矩阵 \(F\)。
沿目标实际 graph 商 \(u+\ell\mapsto\ell-\Phi u\)，其 Lie 映射为
\[
H_{\rm HW}=-\Phi F=-\varepsilon^2\mathcal Q\alpha\pmod p.
\tag{1040.12}
\]
源的模 \(\pi_0\) 恒等高阶基变换，经 Frobenius 后至少在
\(\pi_0^p=\pi_0^{2m+1}\)；
目标的 \(O(\pi_0)\) 误差乘上首层 \(\varepsilon^2\) 也不影响第 \(2m\) 层。
因此 R1038 的真实双端返回矩阵，包括 Schwarzian 对角项，
准确决定 (1040.12) 的首层。

以 \(a\in k[b]/(A)\) 表示 \(\sum_sa(s)e_s\)，取次数 \(<d_A\) 代表。
原 Hasse 方程为
\[
\mathcal L A=0,\qquad
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b .
\tag{1040.13}
\]
令
\[
\mathfrak M(a)=\operatorname{quo}(r^{k_0}a(b)^p,A^2)\pmod A .
\tag{1040.14}
\]
分子 \(\phi=r^{k_0}a^p\) 满足 \(r\phi'=4b^2\phi\)。
故 \(\phi/A^2\) 在各 \(s\in S\) 没有一阶极部，
二阶系数为 \(-q_sa(s)^p\)。
三阶 ODE 比较保留的常数是
\(-q_sa(s)^pS_{\rm GM}(s)/6\)，其中
\[
S_{\rm GM}(b)=\frac{b(b^3+7)}{2r^2}.
\]
所以 (1040.14) 正是 R1038 完整跨尾矩阵的负号版本，
\[
\bar{\mathcal Q}\bar\alpha=\mathfrak M.
\]
实际 \(\bar\alpha\) 在多项式坐标中只对系数作 Frobenius，
因 \(s^{p^2}=s\)。准确的 \(k\)-线性公式于是为
\[
\boxed{\quad
\bar{\mathcal Q}(a)=
 \operatorname{quo}\bigl(r^{k_0}a(b^p),A^2\bigr)\pmod A .
\quad}
\tag{1040.15}
\]
\(a(b^p)\) 保持外部系数不变，不能任换成 \(a(b)^p\)。

特别地，原 \(\lambda=-6(b+1)/r\) 的唯一代表具有
\(\mathbf F_p\) 系数，而
\(r^{k_0}\lambda^p/A^2=-6(b^p+1)/(r^{4g+3}A^2)\)。
R1038 完整首 log 因而在此同一格中是
\[
\boxed{\quad
\bar v=(1-\bar{\mathcal Q})\lambda,\qquad
v=\varepsilon^{-1}e_1\log_B(P_B)\in M_L\otimes R .
\quad}
\tag{1040.16}
\]
定义使用完整 log；右侧只描述它的首层。

## 5. 核准确一维，且负 deck 上单射

对 \(\phi=r^{k_0}a^p\)，取唯一次数 \(<d_A\) 的 \(T\)，使
\[
T\equiv\phi/A'\pmod A.
\]
在各根处，\(TA'-T'A\) 与 \(\phi\) 的零阶、一次 Taylor 相同，
且前者次数 \(<2d_A\)。所以
\[
\phi=A^2P+TA'-T'A,\qquad P=\operatorname{quo}(\phi,A^2).
\tag{1040.17}
\]
再比较二阶 Taylor，使用 (1040.13)，得
\[
P\equiv\frac{\mathcal LT}{2rA'}\pmod A.
\]
于是
\[
\mathfrak M(a)=0\quad\Longleftrightarrow\quad
\mathcal LT=cA\text{ 对某 }c\in k .
\tag{1040.18}
\]
这里 \(a\mapsto T\) 是半线性双射，因为 \(r,A'\) 在 \(S\) 为单位。

直接微分给
\[
\mathcal L(b^e)=e(e-1)b^{e-2}-(e+3/2)^2b^{e+1}.
\]
对 \(0\le e<d_A\)，末系数非零；首个可能零点正是边界
\(e=d_A=(p-3)/2\)。所以 \(\mathcal L\) 在该定义域上单射。
它把
\[
\langle1,b^3,\ldots,b^{6g}\rangle
 \longrightarrow\langle b,b^4,\ldots,b^{6g+1}\rangle
\]
以非零三角对角元映射，两边维数都是 \(2g+1\)。
存在唯一 \(T_0\in k[b^3]\)、\(\deg T_0<d_A\)，满足
\(\mathcal LT_0=A\)。
(1040.18) 的全部解因此是 \(T=cT_0\)，从而
\[
\dim\ker\bar{\mathcal Q}=1.
\tag{1040.19}
\]

对应核元素满足 \(a^p=T_0A'/r^{k_0}\) 于 \(S\)；
右侧在 \(b\mapsto\zeta b\) 下不变。
Frobenius 在这个 reduced 有限代数上可逆，所以核的唯一多项式代表
属于 \(k[b^3]\)。
原 normalized Lie 坐标的真实 deck 是
\[
\delta_*a(b)=\zeta\,a(\zeta b).
\tag{1040.20}
\]
所以核全在 \(\delta_*=\zeta\) 的正角色，
\[
\boxed{\bar{\mathcal Q}\text{ 在负 }\delta_*=\zeta^2
       \text{ 子空间上单射。}}
\tag{1040.21}
\]
本行正、负、旧角色维数分别为 \(2g+1,2g,2g\)；
没有删除旧角色或误用上一行的维数。

## 6. 全部实际 CM 新部在此块中仍为正 deck

### 6.1 排除本行额外的 CM 域

R1010 §3 的完整 CM 域分类在本行除
\(K=\mathbf Q(\sqrt{-3})\) 外，还可能出现
\(K_p=\mathbf Q(\sqrt{-3p})\)。
若 canonical \(\pi\) 为 \(K_p\)-CM，则
\(\pi\otimes\chi_{K_p}\simeq\pi\)。
该 quadratic selftwist 在 \(I_p\) 上是非平凡二次 tame 角色。

写 \(a=p-1,\ N_p=p^2-1\)，实际 \(\tau_1\) 的指数集合是
\(\{a,-a\}\)。二次 twist 加上 \(N_p/2\)；
若保持这个集合，只能交换两项，因而迫
\(4a\equiv0\bmod N_p\)，即 \(p+1\mid4\)，对 \(p>3\) 不可能。
所以
\[
\boxed{\text{实际 }e_1\text{ 块不含任何 }K_p\text{-CM 成分。}}
\tag{1040.22}
\]
此步只排除额外域；还需真实 \(K\)-CM 的 deck 计算。

### 6.2 原完整六层的方向

对任一剩下的 canonical \(K\)-CM 形式，R1010 的实际局部型
在二处只容许 unramified principal 或 unramified Steinberg 的标准二型。
因 \(K\) 在二处 inert，ramified CM induction 的 cusp 型不在其中，
故二处未分歧。三处原指定 cusp 的导子指数二，
CM conductor 公式给 Hecke 角色的 \((\sqrt{-3})\) 指数一。
在 \(p\) 处 \(\tau_1\) 非平凡，Hecke 导子指数亦为一。
因此这些 canonical CM 新形式在 \(9p^2\) 层。

对它们和每个系数嵌入，素于三的理想范数总为 \(1\bmod3\)，
而三处已在导子中；于是
\[
a_n=0\text{ 除非 }n\equiv1\bmod3,\qquad a_2=0,\qquad a_4=-2.
\tag{1040.23}
\]
后式由二处未分歧和平凡中央角色取得，不使用 \(p\bmod4\)。

在原 full-\(6p\) 解析变量 \(\tau\) 中保同一形式的三个二旧方向
\[
H_0=f(\tau/(6p)),\quad H_1=f(\tau/(3p)),\quad
H_2=f(2\tau/(3p)).
\]
R575 的真实 tame 型为 \(1\oplus{\rm Std}_2\)；
\(H_6\) 唯一不变线位于 \(\langle H_0,H_2\rangle\)，
\(H_1\) 平凡二型方向不给 \(H_6\) 不变。
取 \(n=T^{4p}\)，则 \(n\bmod6=T^2,\ n\bmod p=I\)。
(1040.23) 直接给
\(H_0|n=\zeta^2H_0,\ H_2|n=\zeta^2H_2\)。

真正忘去 \(p\) 的六层 Hauptmodul 是
\(u(\tau)=c q^{-1/6}H(q^{1/2})\)。
同一 \(n\) 使 \(u(\tau+4p)=\zeta^{-1}u(\tau)\)，
所以它是实际 \(\delta_\zeta^{-1}\)。
因此原微分线上
\[
\delta_\zeta^*\omega=\zeta\omega.
\tag{1040.24}
\]
\(N_{\rm ns}\) 投影只在 \(p\) 因子，与此 tame 元素交换，
故该方向保留在实际 \(\tau_1\) 固定线上。

这对全部系数嵌入成立。
R575 §4 的完整 Gauss 算子
\(R_0=U_0^*-(U_0^2)^*\)、\(\tau(\chi_{-3})=\zeta-\zeta^2\)
又将 \([\zeta]=(-1+R_0)/2\) 识别为整个 CM Hodge 因子的正嵌入。
原 \(a=\sqrt[3]4\,u\) 的 \(\kappa_4\) 下降同构与 \(\delta\) 交换，
所以不改变方向。
由
\(\langle\delta_*v,\omega\rangle=\langle v,\delta^*\omega\rangle\)，
实际 Lie 推前也具有同一 eigenvalue。
结合 (1040.22)，得到
\[
\boxed{\text{实际 }e_1\text{ 中全部 CM 新 Lie 只有 }
       \delta_*=\zeta\text{。}}
\tag{1040.25}
\]
\(\mathcal Q\) 保持 split-Hecke CM 块又交换正负角色，
因而在这些 CM 新 Lie 上为零；旧部另由 \(D\) 杀掉。

## 7. 原负角色首 log 与完整 MW 饱和消去

R1038 的两个中心都是以原 \(G(b)^2\) 主化。
对 \(\delta_*P\)，它们都变成同一个 \(G(\zeta b)^2\)；
所以原 source 推导逐项给
\[
\lambda_\delta=-\frac{6(\zeta^2b+\zeta)}{1-b^3}.
\]
令
\[
\ell=(p+1)/3,\quad d=(p-5)/6,\quad y=1-b^3,\quad q(y)=Q_p(y),
\]
\[
P_1=T_{\le\ell}\frac1{(1-y)q^2}.
\]
重复真实 degree-\(p\) 返回，使用 \(\zeta^p=\zeta^2\)，
得到实际整负 projector
\[
e_-=\frac{1+\zeta\delta_*+\zeta^2\delta_*^2}{3}
\]
上的首层
\[
e_-e_1\log_B(P_B)\equiv
6\varepsilon\sum_{s\in S}\theta_s
 \frac{s(P_1(y_s)-y_s^\ell)}{y_s^{\ell+1}}f_s
          \pmod{\pi_0^{m+1}} .
\tag{1040.26}
\]
原 \(s=0\) 分量自动为零，其余三根一组由 \(q=0\) 参数化。
R1026 §§1–5 的纯代数定理明确对所有 \(p\equiv5\bmod6\) 有效，
不要求 \(d\) 奇。因此在 \(p>C_*\) 时
\[
e_-\bar v\ne0.
\tag{1040.27}
\]

以完整 (1040.16) 的 \(v\) 定义原整 Lie 泛函
\[
\boxed{\quad
\Lambda_{\mathcal Q}(w)=B(v,\mathcal QD\,e_1w).
\quad}
\tag{1040.28}
\]
只在 formal \(G\)、实际 \(B\) 与 Lie 上使用 \(e_1\)。
R1038 的 prime-to-\(p\) Teichmüller \(\tau\) 先减去，
其 \(B\) 像为零；这里不定义 \(e_1\tau\)。

完整 MW 消去的有理输入由 R1036 §§5–6 支付，
其在给定 non-CM、原 \(D_0\) 非挠 paired block 上的证明
不使用 \(p\bmod4\)：split-Hecke 的本征值生成真正中心 \(F_0\)，
原 \(H_6\) 固定方向一维，原 \(\tau_1\) 的 \(N_{\rm ns}\) 固定线一维，
所以实际 \(J_1\) 的该块是一份 \(C\)，而不是辅助限制标量中的 \(C^2\)；
完整 MW 空间为 \(F_0\beta\)。
本行新增 quadratic PS/St 不在 \(e_1\) 中，不改变该重数。
不同 paired blocks 由 split-Hecke 分离。

于是：原点投影挠性的块第一槽为零；
non-CM 非挠块被 \(F_0\)-平衡交错性全部消去；
旧部由 \(D\) 杀，CM 新部由 (1040.25) 及 \(\mathcal Q\) 杀。
不同块交叉项由 split-Hecke 正交为零。因此
\[
\boxed{\quad
\Lambda_{\mathcal Q}(\log J_1(\mathbf Q))=0,
\quad}
\tag{1040.29}
\]
并消去其与原整 Lie 格相交的饱和格。
这一步没有选取一个未知分母的简单商投影。

当 \(p>C_*\)，(1040.21)、(1040.27) 给
\(\bar{\mathcal Q}e_-\bar v\ne0\)；
它与另一角色的像不能抵消，而 \(D\) 杀旧角色。
由于 \(\mathcal QD\) 为 \(B\)-反自伴，
\[
\Lambda_{\mathcal Q}(w)
 =-B(\mathcal QDv,e_1w).
\]
\(B\) 完美且 \(e_1\) 为原整直和项，所以
\[
\boxed{\quad
\Lambda_{\mathcal Q}\notin
 \pi_0(\operatorname{Lie}\mathcal J_1\otimes R)^\vee .
\quad}
\tag{1040.30}
\]
这是实际整格中的本原性，不是仅证明一个抽象泛函非零。

## 8. 同一原 CM 读数仍需非零

R1039 的原 CM 列在本规范中是
\[
J=\sum_{s\in S}\frac{e_s}{(1-s)^2},\qquad
K_{\mathcal Q,p}=\bar B(\bar v,\bar{\mathcal Q}D J).
\tag{1040.31}
\]
原 \(w=(a-1)/p^3\) 上
\[
F_{\mathcal Q}(w)
 =\Lambda_{\mathcal Q}\left((p\varepsilon)^{-1}
                     \log[P(w)-c_1]\right)
\]
是整级数，约化次数至多 \(n_0=(p-2)/3\)，所有原有理点代入为零。
其最高系数准确为
\[
-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}
       \lambda_0^{-n_0}K_{\mathcal Q,p}.
\tag{1040.32}
\]
原 \(\kappa_1,\lambda_0,A_{\rm tail}\) 均保留；
(1040.30) 不推出这个指定值为单位。

给出保全部 \(\bar{\mathcal Q}^2\) 项的准确读取式。
对系数固定的 \(c\) 取次数 \(<d_A\) 代表，置
\[
\phi_c=r^{k_0}c(b^p),\quad
T_c\equiv\phi_c/A'\pmod A,\quad \deg T_c<d_A,\quad
P_c=\operatorname{quo}(\phi_c,A^2).
\]
同 (1040.17)，
\(\phi_c=A^2P_c+T_cA'-T_c'A\)。
由 (1040.10) 的原配对，
\[
2B(c,J)=(T_c/A)'(1)=P_c(1)
 =\frac{T_c'(1)+(9/16)T_c(1)}{A(1)}.
\tag{1040.33}
\]
使用了原 ODE 的 \(A'(1)/A(1)=-9/16\) 和 \(\phi_c(1)=0\)。
这里是完整商 \(P_c\) 的值；因 \(A(1)\ne0\)，
不能换成其模 \(A\) 剩余类的值。

自伴性给
\[
\boxed{\quad
K_{\mathcal Q,p}
 =\frac12P_{D\bar{\mathcal Q}\bar v}(1),\qquad
\bar v=(1-\bar{\mathcal Q})\lambda .
\quad}
\tag{1040.34}
\]
因此必须保留完整 \(\bar{\mathcal Q}^2\lambda\)。
若核生成元 \(c_0\) 规范为 \(T_{c_0}=T_0,\ \mathcal LT_0=A\)，
在 \(b=1\) 代入得到 \(B(c_0,J)=-1/8\)。
它只说明 \(J\notin\operatorname{im}\bar{\mathcal Q}\)，可能检测 CM 核；
不能替代 (1040.34) 的原 MW 消去读数。

后继须继续证明 (1040.34) 或另一个实际消去读数非零，
并控制原深盘最低单位项。主目标 O1 与 O0 全局覆盖仍开放。

## 来源与审核

- [R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)：原双中心 Raynaud、整 \(e_1\)、双节点共同 Dickson、完整 \(K\)、真实 Hasse 与首 log。
- [R1039](R1039-original-p5-complete-CM-normal-jet-and-rational-disc-scale.md)：本行完整原 CM jet、节点单位、Serre 规范与原有理盘所有分母。
- [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)：以实际 good BT 为前提的两次 PD、真正 Lie 整格和态射自然性。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)：Hermitian 切线证明、实际 split 中心与给定非挠块的原重数一。本文另核 p5 source、双无穷及额外 CM 域。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：graph/Verschiebung 比较与核的纯代数方法；本文给本行真实参数和全部角色维数。
- [R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md) §§1–5：全 \(p\equiv5\bmod6\) 的单余式定理和固定 \(C_*\)。其原 p11 几何应用未被直接挪用。
- [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md) §3、[R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：实际局部型、完整 CM 域及给定非挠 paired block 的半秩来源。
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md) §§2–5：完整 \(6p\) tame 平移、所有系数嵌入的正 CM 作用及原 \(\kappa_4\) 下降；本篇 §6 完整重述所需方向，不恢复旧秩零商。

o1_theta 全文纸核，root 独核双节点 \(C_s^{p-1}/4\)、
本行核维数与原 CM scope；global_route 独核额外域 selftwist 排除。
没有数学程序执行或有限窗口重算。**Serre 主目标仍 OPEN。**
