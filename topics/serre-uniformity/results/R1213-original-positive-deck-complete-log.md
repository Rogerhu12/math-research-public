# R1213：原最高正 deck 首中心的完整 RC–CM 读数

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root。

**已证明。** 本篇将 R1209 的完整首对数计算延伸至原最高惯性权的正自然 deck 部分。输入是给定实际整微分的整个首中心层；其中允许的全纯项不能从 generic 尾底恢复。本篇不将正 deck 的底读取称为单射，不将一个任意中心多项式认作实际纯尖点返回。

## 1. 原对象、输入和精确结论

保持 R1196、R1209、R1211 的同一个模型、原点、有限 Picard 类及实际整角：
$$
p=12g-1=6n+5>37,\quad m=3n+2,\quad a=m^2,\quad
e_0=m(p+1),\quad\pi_0^{e_0}=p,
$$
$$
r=1-b^3,\quad B=b^3,\quad A(b)=bQ(B),\quad
u^m=r^{n+1}A,\quad Q_0=\binom mn,\quad A_1=A(1)=-Q_0.
$$
置 $L=(m-1)/2$、$c_m=(-1)^L\binom{m-1}{L}$、
$\nu=(-3)^L(2\gamma)^{m-1}$，全为 R1209 的原规范。

给定实际微分
$$
\Omega\in E_m\Lambda,\qquad
\sigma^*\Omega=\xi^{a}\Omega,\qquad
\delta^*\Omega=\zeta\Omega.
\tag{1213.1}
$$
它的原首中心层必唯一写成
$$
\overline{\pi_0^{-1}\Omega}|_I
=\eta_S=\frac{S(b)}{uA(b)}\,db,\qquad
S(b)=b\,P(B),\quad \deg P\le n.
\tag{1213.2}
$$
这里除 $\pi_0$ 只沿中心读取，不称整个 $\Omega$ 可除 $\pi_0$。
次数界及可能的极点由 R1193.12 的全角色论证给出；正 deck 将分子角色换成 $b\,k[B]$。在所有 $A(s)=0$ 上的值只决定 $S\bmod kA$；$S=A$ 对应原全纯 $db/u$，始终保留。

定义同一原首值
$$
\mathcal V_m^+(S)
=\overline{\pi_0^{-a}\langle E_m\log((p-1)D_0),\Omega\rangle}.
\tag{1213.3}
$$
它在所有实际出现的 $S$ 上只依赖整个 (1213.2)。确实，相同 $S$ 先给相同 SS polar parts，从而给相同 generic 底。两个提升的差因此特殊约化为零；唯一能在所需精度出现的低中心权是 $a-1$，须乘 $\pi_0$，其整个全纯空间为 $k\,db/u$，而相同 (1213.2) 已把它消去。其余允许的权差首代表至少为
$e_0-p=2m^2-1>a$，同权差至少为 $e_0$。故其配对不贡献目标 normal。此论证不把“相同底”偷换成“相同首中心”。

保持同一个 good CM 周期
$$
F(X)={}_2F_1(1/6,1/6;2/3;X),\qquad
G(X)={}_2F_1(1/2,1/2;4/3;X),
$$
$$
X=v^3,\quad b=(1-X)^{1/3},\quad
t=vG/F,\qquad
\mathcal E_S(t)=-\frac{v^2F^3S(b)}{A_1}
=\sum_{k\ge1}e_{k-1}(S)t^{3k-1}.
\tag{1213.4}
$$
所用全部系数在次数 $<p$ 的原有限 PD 比较内。结论为
$$
\boxed{\quad
\mathcal V_m^+(S)
=-\frac{8\,2^m\nu}{A_1}\,e_n(S)
=-\frac{8\,2^m\nu}{A_1}[t^m]\mathcal E_S(t).
\quad}
\tag{1213.5}
$$
这与 R1209 形式相同，但其证明的 surviving 对称分量不同。

## 2. 全部 SS normal 与真正留下的 $\lambda_0$

R1199 §§2–4 的完整 normal 论证只使用最高 $\sigma$ 权、$E_m$、首中心极界和 full framing；没有使用负 deck。它在给定 (1213.2) 时逐字给同样的 $\mathcal E_{s,S}$、$\gamma_{N,s}$ 与完整 $\omega_{N,s}$，包括 $S(s)=0$ 时从中心正则项传入的较高 normal。其一维角像排除了低极及 holomorphic 的额外自由项，不能因 generic 底为零便删除 $S=A$。

将原 $\lambda=-6(b+1)/r$ 分为
$$
\lambda_0=-6/r,\qquad\lambda_1=-6b/r.
$$
同 R1200.32 的有限 ODE 缩放，现在 $S(\zeta b)=\zeta S(b)$，故
$$
\mathcal P_m^{\lambda_\epsilon}(S)(\zeta b)
=\zeta^{\epsilon}\mathcal P_m^{\lambda_\epsilon}(S)(b).
$$
因此整个 SS 和只留下 $\lambda_0$；$\lambda_1$ 沿每个非零三轨相消，在固定根 $s=0$ 也为零。置
$$
\mathcal P_m^{\lambda_0}(S)(b)=\mathsf P(B),\qquad
\deg\mathsf P\le3n+1.
$$
实际 SS 部分于是为
$$
\mathcal V_{\rm SS}^+(S)
=-mc_m\nu\sum_{A(s)=0}
\frac{\mathsf P(s^3)}{r(s)^{n+2}A'(s)^2}.
\tag{1213.6}
$$
这是完整收缩之后的对称消去，未在单个节点改动原 log。

R1209 的低阶 Rankin–Cohen primitive 仍成立。次数界需相应核准：$\lambda_0$ 的分子较 $\lambda_1$ 少一次，而 $S=bP$ 较原 $P(B)$ 多一次，故
$$
K_{0,b}^{(i)}\in r^{-i-1}k[b]_{\le2i},\qquad
E_{b,j}\in r^{n+2-j}k[b]_{\le3n+1+2j}.
$$
在 $i+j=m-2$ 时仍有
$$
\mathcal T_b\in r^{n+3-m}k[b]_{\le9n+1},\qquad
\mathcal J_S=3b^pr^{m-1}\mathcal T_b
=b^pr^{n+2}R_S(b),
$$
$$
R_S\in b\,k[B],\qquad \deg_b\mathcal J_S\le3p-3.
$$
其中 $R_S$ 的角色由 $S$ 权一与 $\lambda_0$ 权零之和决定，与 R1209 的总角色相同。因此
$\mathcal J_S=J_S(B)\in B^{2n+2}(1-B)^{n+2}k[B]$、
$\deg J_S\le p-1$，且
$$
J_S'=B^{2n+1}(1-B)^{n+1}\mathsf P(B).
$$
原合法积分严格为零；全部次数仍至多 $p-2$。

## 3. 原 Gauss 误差及 SS 的两个部分

R1209 §5 的误差
$$
\Delta(1-X)=\frac{3F(X)}{Q_0Q(X)}
=\frac{3bF(X)}{Q_0^2G(X)}
\pmod{X^{n+1}}
$$
只依赖原 $Q$，故不变。上节给相同多项式次数及积分零，故其 $0$ 端精确抵消原固定 SS 节点，其 $1$ 端 residue 公式亦不变。

唯一改动是在原 good gauge 中使用
$$
K_0(t)=\frac{6F^2}{v}=\frac6t+L_0'(t),\qquad
L_0(t)=\sum_{j\ge1}\ell_j^{(0)}t^{3j}.
$$
R1209.24 的 same-source 运输对任意 $\lambda$ 线性，现在给
$$
\mathsf P(b^3)
=-v^{m-2}F^{-p-2}\mathfrak C_m(K_0,-A_1\mathcal E_S).
$$
所有 ramification 三、$F^{-p}$ 高阶界和前置单位均不变。置
$$
\mathcal A_S^{(0)}
=\sum_{\substack{j,k\ge1\\j+k=n+1}}
\frac{(-1)^{k-1}\ell_j^{(0)}e_{k-1}(S)}
{(3j-1)!(3k+1)!}.
$$
R1209 的两项有限 RC 计算便准确给
$$
\mathcal V_{\rm SS}^+(S)
=-\frac{16c_m\nu}{A_1}e_n(S)
+\frac{2c_m\nu m!}{A_1}\mathcal A_S^{(0)}.
\tag{1213.7}
$$
特别 $6/t$ 的 singular 项仍在，未将 $K_0$ 误作 regular 输入。

## 4. 三个原 CM 尾的相位与全 mixed-normal

在 $b_\xi=\xi b$、$\xi^3=1$，周期 $t$ 和 R1209 的实际 $c_\xi,\tau_\xi$ 不变。现在
$$
S(b_\xi)=\xi S(b),\qquad
\mathcal E_{S,\xi}(t)=\xi\mathcal E_S(t).
$$
所以每个原完整 mixed-normal 为
$$
\Omega_{\xi}^{[N_k]}
=\gamma_{k,\xi}^+(S)\,dH_k,\qquad
N_k=(3k-1)m,\quad d_k=(N_k-1)/3,
$$
$$
\gamma_{k,\xi}^+(S)
=\frac{mc_\xi^{3k}\xi}{3\tau_\xi d_k}\,e_{k-1}(S),
\qquad1\le k\le n+1.
\tag{1213.8}
$$
极界与完整一维角像来自 R1209 §3，均未使用该系数是否独立于 $\xi$。顶层原 $\mathrm{St}^N=0$ 也保持。

原三个支持的合法 analytic log 仍为
$$
L_\xi=\xi^2L_1+\xi L_0,\qquad a_\xi=\xi^2+\xi,
$$
而原节点相位为
$$
\frac{c_\xi^{m+1}(A_\xi^{\rm tail})^L}{\tau_\xi}
=\frac{\nu\xi}{A_1}.
$$
现在额外的 $\xi$ 来自 (1213.8)，故实际所取和是
$$
\sum_{\xi^3=1}\xi^2L_\xi=3L_0.
$$
完整 residue 及 $j+k=n+1$ 选择与 R1209.31–34 相同，准确得到
$$
\mathcal V_{\rm CM,an}^+(S)
=\frac{3mc_m\nu(m-2)!}{A_1}\mathcal A_S^{(0)}.
\tag{1213.9}
$$
由 $2m!+3m(m-2)!=0$，它与 (1213.7) 的全部 regular 部分逐项抵消。

## 5. 原 static 单位与最终公式

原 node frame 仍使用
$\sigma_\xi=(1+A_\xi^{\rm tail}z_D^{4g})^{-3a_\xi}$，
并保留 centre–node 接口。R1208/R1209 的有限 static residue 给
$$
\operatorname{Res}_\infty
[-3a_\xi\log(1+A_\xi^{\rm tail}z_D^{4g})]\,dH_{n+1}
=4a_\xi(2c_m-2^m)(A_\xi^{\rm tail})^L.
$$
式 (1213.8) 在顶层额外乘 $\xi$，而
$$
\sum_{\xi^3=1}a_\xi\xi^2
=\sum_{\xi^3=1}(\xi^4+\xi^3)=3.
$$
所以
$$
\mathcal V_{\rm CM,st}^+(S)
=\frac{8\nu}{A_1}(2c_m-2^m)e_n(S).
\tag{1213.10}
$$
同 R1209，static 过渡的隐藏 $p$ 分母返回严格超出目标精度；不在整个 node 上对非 $1+I$ 的函数取 log。加总 (1213.7)、(1213.9)、(1213.10) 即得 (1213.5)。

也可在已经支付全部接口后写成原端点评价：
$$
\mathcal V_m^+(S)
=\sum_{\xi^3=1}a_\xi\gamma_{n+1,\xi}^+(S)H_{n+1}(Q_\xi).
\tag{1213.11}
$$
此式沿用实际 $H_{n+1}(Q_\xi)=-4\,2^m(A_\xi^{\rm tail})^L$；不是用另选函数值定义新对数。

## 6. 与实际纯尖点格之间仍须保留的区别

R1211 已给同一最高角色全部 deck 上 $q=e_{V_m}e_N$ 的整性。
R1205.11、1205.14 又给原正纯尖点秩 $n+1$；正 generic 底只有 $n$ 维。这一差异与本篇保留的 $kA$ 方向一致，但维数本身不支付实际格映射。

特别原正高 PS 输入为 $T\in k[B]_{\le n}$；R1204 的实际 generic 返回证明给
$S\bmod kA=-3\gamma^2\mathscr DT\bmod kA$，其中
$$
\mathscr D=(1-b^3)\partial_b^2-4b^2\partial_b-\frac94b.
$$
它的代数三角式是
$$
\mathscr D(B^j)
=b\left(3j(3j-1)B^{j-1}
-\frac94(2j+1)^2B^j\right).
$$
故这个多项式算子从 $k[B]_{\le n}$ 到 $b\,k[B]_{\le n}$ 为同构；然而仅凭 SS 返回值不能把 actual 首中心中的额外 $A$ 系数设为零。若实际首中心已被付为某个 $S$，方可用 (1213.5) 读取该向量。

本篇不新增 $db/u$ 的模权/CM 身份结论（R1028.9、R918 已有），不把其模 $p$ 身份当成原 varying-weight 主系列的整分裂（R970 已区分）。指定 $C$、whole MW 饱和格、两 deck 的 $\Pi/\Phi$ 与极化比较继续保留。

来源：R1193 §§3–5、R1196 §§1–6、R1199 §§2–5、R1200 §§6/8.1、R1208 §§3–6、R1209 §§2–8、R1211；均为同一个原模型上的纸面运输。没有执行数学程序或新窗口。

global_route独立逐节纸核PASS：同一首中心的提升独立、λ₀全部次数界/固定根消去、CM额外ξ、analytic与static两个三次和以及D的三角式全部核准。只对actual首中心读取，不附送pure返回的A系数。
