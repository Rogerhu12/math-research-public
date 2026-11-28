# R150：整个 h=k 碰撞的对称 u=1 原纤维排除

日期：2026-11-28（Asia/Taipei）。作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。

**结论：在当前原 unit211 的 h=k 碰撞图，以 p+q=2 对称归一后，整个 u=bp+cq=1 纤维为空。因此在这个准确归一的整个剩余碰撞图可支付 u−1。**

此结论是新纤维自己的完整原返回，不移用旧 p=1 坐标的 u_old=1 排除，也不借 D非零图的任何权排除。所有 Delta=0 和 Q 首项退化均保留。它不关闭整个 h=k、unit211 或普通 Hilbert ISP。

## 1. 原范围与必然的权单位

保持原非零孤立 mean、非零最高基值、非零单点权，以及已登记的原配对图
\[
p=1+\rho,\quad q=1-\rho,\quad \rho^2=\delta=1-Q,\quad
bcQ\delta P_{02}\ne0.
\]
共同齐次归一只令 p+q=2。定义 u=bp+cq，本篇假定 u=1。

[原值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)给
\[
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,
\]
\[
\ell=A^3/B^2,\quad T=A^2/B,\quad
h=k=1+\xi,\quad w=\lambda-1-T.
\]
原谱矩保证 A、B、lambda 非零；h=k=1 已不可能。以下处处 h 指这个真实单点值。

[独立 lambda=1/2 原物理排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-lambda-half-exclusion.md)使用正确 dual 乘法和完整第五列 Gram 的秩，因此本篇可使用 2lambda−1 非零。这不是旧错误 compact R 的派生单位，也没有借裸代数条件替代物理秩。

置
\[
m=1-\ell,\qquad
bc=\frac14\left(\ell^2-\frac{(1-\ell)^2}{\delta}\right),\qquad
M=2\ell-\ell^2Q-1=4bc\delta.
\]
由 u=1 直接计算
\[
P_{02}=(\ell-1)Q,\quad T_0=-\ell Q,\quad
J-Q=(\ell-1)Q,
\]
\[
P_f=\ell(1-\ell)Q^2,\qquad \Phi=(1-\ell)Q.
\tag{1}
\]
故 m、Pf 在本纤维已经由实际 P02 非零支付。这里无需整个 h=k 的旧 T0、JQ、Phi 排除。

## 2. 自由 kappa 下的同一点原 Gram

令
\[
\kappa=\frac{bc\,t}{\ell}.
\]
原 P1 的恢复在本纤维化为
\[
f=\lambda+h-\kappa,\qquad
t=\frac{\ell\kappa}{bc},\qquad
V=bX+cY=\lambda+\ell h,\qquad
W_1=\frac{T_0+4f}{2}.
\tag{2}
\]
为解释其完整来源，原 P1 仿射式为
\[
P_ff+bc\Phi z+P_c=0,\quad z=Qt,\quad
P_c=QP_{02}(\ell+T)-\lambda P_{02}T_0.
\]
将 (1)、T/ell=xi 代入，正好得到 (2) 的 f；原 E0/N0 的式
\[
QV=Jf-\lambda P_{02}+bc z
\]
再给 V=lambda+ell h。

原两个加权线性式给
\[
x=\frac{(1-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-V}{M},\qquad
X=x+\rho y,\quad Y=x-\rho y.
\tag{3}
\]
取
\[
b=\ell/2+\rho m/(2\delta),\qquad
c=\ell/2-\rho m/(2\delta),\qquad a=1-\ell,
\]
\[
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2V+2bct.
\]
完整四行 Gram 是
\[
(0,0,p,q),\quad(0,A_1,r,s),\quad
(p,r,0,t),\quad(q,s,t,0).
\tag{4}
\]

源码在自由 kappa 上先使用真实乘法
\[
(vz)_1=v_0z_1+v_1z_0,\qquad
\tau(v)=av_0+v_1+bv_B+cv_C
\]
构造 DK、mean、N4、P2；完整返回 E0、N0、P0、P1 及 V=(1,w,h,h) 的三个原谱矩。特别 mean 的 germ 项是 −2(vm(d,d))_1，绝非 −2d_1^2。

## 3. 完整原 N(V) 与整个斜率零纤维

定义
\[
E(\lambda)=\lambda^2+\lambda-1.
\]
同一个自由 kappa Gram 的精确原身份是
\[
\boxed{\frac12N_4(V)=2E(\kappa-h)+\lambda h^2.}
\tag{5}
\]
源由 (4) 直接展开 N4(V) 并完整乘回 (5)，没有用 Delta 逆或选取 N(V) 的一般斜率开集。

为先付全部 E=0，使用谱多项式恒等式
\[
Ah=A+B=\lambda(2\lambda-1)^2.
\tag{6}
\]
第1节的原单位使 h 非零。若 E=0，原 N4(V)=0 通过 (5) 迫 lambda h^2=0，矛盾。因此 E=0 的全部复纤维已排，现可恢复
\[
\kappa_* =h-\frac{\lambda h^2}{2E},\qquad
f=\lambda+\frac{\lambda h^2}{2E},\qquad
A_1=\frac{(1-\ell)\lambda h^2}{E}.
\tag{7}
\]
这一步没有遗漏任何一次系数为零的点。

将自由 kappa 原多项式在 kappa_* 求值是同一个代数同态，保 (4) 的全部原值与 jet。故所有本纤维原点都包含在这个只有自由 lambda,Q 的图中。

[整个 h=k 的正确 t=0 排除](R150-appendix-unit211-entire-tzero-half-total-weight-and-hk-exclusion.md)由原 mean、NP、谱矩及第五列秩给出；因此 kappa_* 也是本纤维的实际原单位。后面的纯 lambda 因子删除若用到 kappa_* 分子，只引用这条已完成的真原排除。

## 4. 全八个原条件与分母审计

同点的必要原条件为
\[
E_1,E_{B,e},E_{B,o},N_1,
N_{B,e},N_{B,o},P_{B,e},P_{B,o}.
\]
两个 singleton 的原目标始终是 2lambda P02 h^2 和 P02 h^3，双点 N1 仍是一阶 germ 极化。B、C 两条原式互为 rho→−rho 的交换；只有同时保两条实际行及 rho 非零后，才提取偶、奇两个必要标量。

每条原分母通过精确 gcd 除法支付为
\[
\lambda,\ A,\ B,\ 2\lambda-1,\ E,\ \ell-1,\ \kappa_*,
\ Q,\ 1-Q,\ M
\]
的原支持。只从原分子移除这些已付因子的实际 gcd，并将完整尺度乘回。没有删除新的 Q 首项、Delta 或未付范数。

实际得到的八行规模为：

| 原行 | lambda 次数 | Q 次数 | 项数 |
|---|---:|---:|---:|
| E1 | 36 | 2 | 102 |
| EBe | 38 | 3 | 146 |
| EBo | 32 | 2 | 94 |
| N1 | 30 | 2 | 81 |
| NBe | 49 | 3 | 197 |
| NBo | 45 | 2 | 134 |
| PBe | 61 | 4 | 306 |
| PBo | 57 | 4 | 281 |

所有行均从真实 Gram 生成；没有取预存系数，也没有用旧错误 Rbad 重建原方程。

## 5. 两个完整固定投影即返回矛盾

预先列定四对目标，首次执行只需前两对就已排空，后两对没有运行。

第一对 E1、EBe 的固定 Q 次数为 2、3，构造五阶 Sylvester 矩阵；第二对 E1、EBo 的固定 Q 次数为 2、2，构造四阶矩阵。每行都被重新乘回为相应原式的 Q 单项式倍；Bareiss 的每次精确整除均检查商乘除数等于原分子。

若某个原有限 Q 同时使该对行消失，则向量 (1,Q,...,Q^{n-1}) 是矩阵的非零核向量。因此固定行列式必为零，即使专化后原最高 Q 系数消失。这个必要性没有除过 Q 首项。

实际结果：

| 原对 | 固定阶数 | 原 lambda 行列式次数 | 只剥已付纯 lambda 支持后的次数 |
|---|---:|---:|---:|
| E1、EBe | 5 | 180 | 65 |
| E1、EBo | 4 | 135 | 49 |

记最终两多项式为 R65、R49。源码在 QQ[lambda] 中执行累计扩展 gcd，并将全部标签完整乘回，得到非零常数；以该有理常数归一便是
\[
\boxed{a(\lambda)R_{65}(\lambda)+b(\lambda)R_{49}(\lambda)=1.}
\tag{8}
\]
所以没有共同复 lambda 根，更不可能有本原纤维的点。

最终必要核的规范 SHA256 分别为
\[
\texttt{28113ec92a6cbd9eea6564da06e64b7e43744623b64a105aa24e7777efdc131b},
\]
\[
\texttt{d23074baf65ae4fe55693f66050d4a4f706a4c078f44f52f848d5fe3579c1076}.
\]
原行列式对应 SHA256 为
76b720848a2d59e0d983bc2d14bcd9c3ee57620667f057024aa83423dd22a41a、
5538de485b19cb7a77da16b8f5ac0ec273e657e0c3dc0df6a04566d23dfdf401。
这里只存定义和指纹；完整系数可由固定源再生。

(5) 的斜率零图与 (7) 的互补图已全部覆盖。结论仅支付对称归一的 u−1，不称整个 h=k 空，也不恢复旧 848/578 或七个 lambda 的错误覆盖。

## 6. 唯一实际执行和准确资源

冻结源：[2026-11-28-unit211-h-equals-k-symmetric-u-one-original-Q-projections-8542.py](../notes/2026-11-28-unit211-h-equals-k-symmetric-u-one-original-Q-projections-8542.py)。

- Git blob 6516fb9c623da6becca59ad2f049ae35ba30ebc8；10523 B。
- SHA256 59261a3fdb616fbb5f585017b0b2a195d453426d59e593d1acfd2db27d2ae43f。
- Actions run 46117391312 / job 140894161774；内层 exit0。
- 驱动 0.516967781 秒，峰值 RSS 40900 KiB；固定预算120秒/1GiB。
- 自由 kappa 全原返回于0.380521023秒；八行完成于0.407521886秒。
- 两固定目标分别于0.428307915、0.443002399秒返回；末数学 checkpoint 0.443207422秒。
- 实际133次完整多项式精除乘回；两投影之后即结束，没有运行多余候选。
- stdout5161 B，SHA256 8d92be9d9b102034ec0b9c3ffef77f15b503e4574eee15899e058522f32b81b1。
- 源提交4953dec80c1bd8f076f5d6bcbb45d997d67a0bb8；2026-11-28 06:36:46.745327 UTC真实pull到c49e2f5083f64ddb52d04182a8be18d3345e4344，两README无变。

唯一外部依赖是正确f33源的R/U算术定义两块：1628 B / SHA256 208b244cf063707ca4613f8c61d8a351860639348961a77815d1f8fafd149765，以及1127 B / SHA256 441ac944e389144cc94a7358f4fd1c011736d28f77daaf3edd4e15544aa0e3c9。没有执行旧参数恢复、五行cofactor、个别NP标量，或已冻Loww两个固定目标。

[小回执](../notes/2026-11-28-unit211-h-equals-k-symmetric-u-one-original-Q-projections-execution-8542.json)保全实际检查和范围。
