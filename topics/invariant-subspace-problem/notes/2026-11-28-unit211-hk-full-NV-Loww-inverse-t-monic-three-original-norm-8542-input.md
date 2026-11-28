# 新输入：h=k 的完整 NV–Loww 倒 t 首一三次及原两源范数

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

**同一未完成输入的工程修复版，修订源尚未执行。** 原 e9bd 唯一首次在 pp 的 fmpz 指数 JSON 序列化处 exit 1；完整来源及准确范围见同 stem 的 first-JSON-failure.md 与 first-JSON-failure.json。修订仅将 pp 指数、degree 显式转成 Python int，全部数学和原预算不变。本输入定义完整 NV 与完整 Loww 的同点三维乘法范数。没有预记非零范数、权曲线、有限性或排空。旧 E1–Loww、EBo–Loww 两个固定投影继续冻结。

## 1. 当前原图、来源及查重边界

采用已刊正确碰撞图，记
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\delta=1-Q,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad
T=A^2/B,\quad h=k=1+\xi,\quad w=\lambda-1-T.
\tag{1}
$$
本门所用权环只倒
$$
A\,B\,Q\,\delta\,P_f\,M\,P_{02}\,\lambda(2\lambda-1),
\qquad M=4bc\delta.
\tag{2}
$$
其中 $P_f=T_0(J-Q)$。这些都是当前正确原图的既有单位；$\lambda\ne0$ 是原均值图条件，整 $\lambda=1/2$ 已由独立第五列物理秩排除。没有新的 $\Delta,T_{\rm num},\Phi,u,u-1,\ell,m,S$ 逆，没有新 Loww 首项或范数逆。即使其中某些面已被别的定理关闭，本源也不借此约掉原式。

原恢复与完整 NV 来自
[正确五行坐标源码](2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py)
和
[完整个别 N/P 及 NV 原值源码](2026-11-28-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns-8542.py)。
后者的真实双数乘法已完整返回
$$
Q\,N_4((1,w,h,h))=2\,NV.
\tag{3}
$$
(3) 包含原值的全部项，不是某个系数或某个参数倍数取代原值。

完整 Loww 来源是
[旧首次输入](2026-11-28-unit211-h-equals-k-original-low-weighted-two-fixed-z-projections-8542.md)
和
[准确冻结回执](2026-11-28-unit211-hk-original-low-weighted-two-projections-resource-boundary-8542.json)。
该唯一旧 run46115251930 在 180.050586477 秒以 SIGALRM 结束；已返回完整原 Loww 身份及三行清分母，两个固定目标均未返回。冻结目标仅为
$$
\operatorname{Res}_z(E_1,Loww),\qquad
\operatorname{Res}_z(E_B^{odd},Loww).
$$
本次不重生、改变顺序或延长它们，也不重生四个旧 individual N/P–NV 标量。

已只读核对当前 log/open/HANDOFF、旧 Loww 输入/冻结回执和相关 notes 索引，未找到完整 HK NV–Loww 的 Norm/adj 成败记录；此前正确 $\Delta=0$ 两谱域里使用的是原 E1 与倒 z Loww 的有限常数域返回，与本次一般三参数 NV 范数不同。此处只是输入查重记录，不是新的数学审核门。

## 2. 同一个原 t 的完整两式

仍使用
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,\quad
P_f=T_0(J-Q).
$$
固定原谱后
$$
f(t)=-\frac{P_c+bcQ\Phi t}{P_f},\qquad
V(t)=\frac{Jf-G+bcQt}{Q},\qquad
W_1(t)=\frac{T_0+4uf}{2}.
\tag{4}
$$
记
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad m=u-\ell.
\tag{5}
$$
原两个 singleton 均值为 $X=x+\rho y,Y=x-\rho y$，其中 $\rho^2=\delta$。本门不需要选 $\rho$ 符号。

完整 NV 的系数为
$$
S=2\xi+3-2\lambda,\qquad \eta=\xi+3-2\lambda,
$$
$$
N_F=(3-4\lambda)Q+J\xi\eta,\qquad
N_C=\eta(-G\xi+Qwu),
$$
$$
NV(t)=N_Ff(t)+bcQS\xi\,t+N_C.
\tag{6}
$$
定义
$$
\Delta=\Phi N_F-S\xi P_f,\qquad
T_{\rm num}=P_fN_C-P_cN_F.
$$
因此整式
$$
n(t):=P_fNV(t)=T_{\rm num}-bcQ\Delta\,t
\tag{7}
$$
按完整原 (6) 返回。既不除 $\Delta$，也不除 $T_{\rm num}$。

当 $p+q=2$，已付完整原式为
$$
K_w=2[t^2+(5u-4x-2)t+2(x^2-\delta y^2)
+4x+4\delta y-4ux+2u^2-6u+Q],
$$
$$
L(t):=Loww
=2P_{02}(2\lambda-1)w-bct[K_w+4(f-u)(t-2)].
\tag{8}
$$
它与 (4)–(7) 是同一个 $t$。自由 $f$ 的修正项 $4(f-u)(t-2)$ 完整保留。既有原身份是
$$
L=NS-PS+E_{W2},\qquad
E_{W2}=b(2p-u-X)E_B+c(2q-u-Y)E_C,
\tag{9}
$$
其中
$$
NS=bN_4(g_B)+cN_4(g_C)-2\lambda P_{02}\ell h^2,
$$
$$
PS=bP_2(g_B)+cP_2(g_C)-P_{02}\ell h^3.
$$
因此本次两式均有完整原理想来源，不把必要低组合称为整个原系统。

## 3. 显式倒 t 首一三次，不用存在性系数

(4)–(5) 对 $t$ 仿射，所以 (8) 次数至多三。它的常数为
$$
c_0=L(0)=2P_{02}(2\lambda-1)w
=-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B},
\tag{10}
$$
这里用的是原恒等式
$$
w=-\lambda^2(2\lambda-1)/B.
$$
由 (2)，$c_0$ 是既有权单位。源码按系数返回 (10)，并检查其分子、分母都只含 (2) 支持。

事实上，写 $L=c_0+tL_1$，则
$$
v=-L_1/c_0,\qquad tv-1=-L/c_0.
\tag{11}
$$
所以 $t$ 在两源商里本身已有多项式逆。这里不需要额外几何局部化。已刊
[整个 t=0 原排除](../results/R150-appendix-unit211-entire-tzero-half-total-weight-and-hk-exclusion.md)
与 (11) 的当前图结论相容，但本次 (11) 有直接系数返回。

取 $\zeta=1/t$，定义
$$
q(\zeta)=\zeta^3L(1/\zeta)/c_0
=\zeta^3+q_2\zeta^2+q_1\zeta+q_0.
\tag{12}
$$
这是整权环上的真实首一三次。它保留 $L$ 的三次、二次或更低系数下降；特别是 $q_0=0$ 时也不删除该纤维。$R[\zeta]/(q)$ 自由秩三只是新多项式环境；它不等于已经满足全部原值条件的商。

反转 (7)：
$$
a(\zeta)=\zeta n(1/\zeta)
=\alpha+\beta\zeta,\qquad
\alpha=-bcQ\Delta,\quad\beta=T_{\rm num}.
\tag{13}
$$
$\alpha,\beta$ 都可能为零，均不作为单位。

## 4. 三真实乘法列、伴随列及全多项式 lift

在基 $1,\zeta,\zeta^2$ 上，源码逐列作首一短除，并完整返回
$$
a\zeta^j=M_{\bullet j}\cdot(1,\zeta,\zeta^2)+Q_jq
\quad (j=0,1,2).
\tag{14}
$$
因此
$$
M=
\begin{pmatrix}
\alpha&0&-\beta q_0\\
\beta&\alpha&-\beta q_1\\
0&\beta&\alpha-\beta q_2
\end{pmatrix}.
$$
新标量及第一伴随列是
$$
\mathcal N=\det M
=\alpha^3-\alpha^2\beta q_2+\alpha\beta^2q_1-\beta^3q_0,
\tag{15}
$$
$$
b(\zeta)=
(\alpha^2-\alpha\beta q_2+\beta^2q_1)
+(-\alpha\beta+\beta^2q_2)\zeta+\beta^2\zeta^2.
$$
源码由真实 $2\times2$ cofactor 构造该列，并对三个坐标全部返回
$$
M\,\operatorname{adj}(M)e_0=\mathcal N e_0.
$$
继而利用 (14) 返回完整多项式，而不只返回商中的零：
$$
a(\zeta)b(\zeta)-\beta^3q(\zeta)=\mathcal N.
\tag{16}
$$
所有恒等式在权多项式/旧单位局部化环内成立，故保 $\alpha=0,\beta=0$、矩阵临时秩下降、全部新范数零集。没有抽象秩测试或裸模返回。

## 5. 回到完整 NV 与 Loww；只取消真实乘子

用 (12)–(13) 将 (16) 乘 $t^3$，得到
$$
\Omega(t)NV(t)+\Theta L(t)=\mathcal N t^3,
\tag{17}
$$
$$
\Omega(t)=P_ft^2b(1/t),\qquad
\Theta=-\beta^3/c_0.
$$
$\Omega$ 是 $t$ 至多二次。源码逐原 $t$ 系数完整返回 (17)。

随后仅对 $\Omega,\Theta,\mathcal N$ 的实际旧权分母取 LCM，检查每个分母只含 (2) 支持。清分母后，取所有原乘子系数和标量的共同多项式因子；每一项真实精除乘回，再次对完整原 NV、Loww 返回
$$
\Omega_*NV+\Theta_*L=S\,t^3.
\tag{18}
$$
共同因子不被当成单位；(18) 直接是除后实际乘子的新原组合，所以其整个零纤维仍在。把标量纳入共同因子，确保没有通过原有理式系数分母假设未经证明的整除。

最后只剥 $S$ 的旧已付纯权支持，得
$$
S=U_{\rm paid}P.
\tag{19}
$$
实际保留的完整身份是
$$
\Omega_*NV+\Theta_*L=U_{\rm paid}P\,t^3.
\tag{20}
$$
新 $P$ 的所有零集保留；若 $\mathcal N$ 或 $P$ 恒零，照实记录，没有新非零曲线结论。这里不计算 QQ 因式、第二个旧目标或 QQ gcd。

(11) 还能给明确纯权两源来源。令 $r=L/c_0$，则 $tv=1-r$；由
$$
1-(1-r)^3=3r-3r^2+r^3
$$
及 (20)，得到
$$
P=\frac{v^3\Omega_*}{U_{\rm paid}}\,NV+
\left[
\frac{v^3\Theta_*}{U_{\rm paid}}
+P\left(\frac3{c_0}-\frac{3L}{c_0^2}+\frac{L^2}{c_0^3}\right)
\right]L.
\tag{21}
$$
这是已返回 (11)、(20) 的有限乘法表达式，不加任何新的逆。源码不展开 (21) 的高次原乘子，也不冒称保存了展开证书；(21) 的通用三次几何级数证明已完整写在这里。

即使 $P\ne0$，单一新权必要式也不单独给有限权集或排空。完整原 Gram/N/P 系统始终保留。

## 6. 唯一必要前缀与冻结资源

唯一依赖是正确 f33 原源码，完整 SHA256：

2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。

截在 “# Exact scalar forms” 之前，4540 字节，SHA256：

a56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc。

AST 仅移除旧顶层时钟/资源调用、旧顶层 assert 和旧 say 输出；保留算术类、原坐标及参数定义。旧依赖不会重置外层绝对截止，也不会降低硬内存界。源码不加载 bb534/dc888 的证明尾，只以上面准确来源引用其已返回原身份。

新源 basename：

2026-11-28-unit211-hk-full-NV-Loww-inverse-t-monic-three-original-norm-8542.py。

源码 SHA256：039f4dd37cbe91d03c12465c62b637f177fee7bf227b39e9335833ddd3f52fda。

UTF-8：10014 字节。唯一首次预算 **180 秒 / 4 GiB，外层 195 秒**。

仅保源码、参数定义、次数/项数/字节数/SHA、小回执及准确完成范围。没有系数载荷、编码分片或矩阵缓存。若触界，仅登记最后完整 checkpoint，冻结该目标，不恢复、不换序、不加时重算。
