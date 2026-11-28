# 新输入：对称归一 h=k 的整个 u=1 原纤维

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127，GPT-6 Astra Pro（AI-assisted）。

本源未执行，不预记消元、有限或排空结论。固定 120 秒 / 1 GiB；不重放已完成的 h=k 五行 cofactor、四个个别 NP 标量，或已冻的 Loww 两投影。

## 1. 准确原范围

保持原 h=k 碰撞、非零孤立 mean、原 P02、b,c,Q,1-Q 非零，并采用
\[
p=1+\rho,\quad q=1-\rho,\quad \rho^2=1-Q,\qquad u=bp+cq=1.
\]
这是 p+q=2 的对称坐标；旧 p=1 图的 u_old=1 排除不等同此纤维，故不借其单位。

原谱矩图给
\[
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
\]
\[
h=k=1+\xi,\quad w=\lambda-1-T.
\]
A、B、lambda 是原单位；lambda=1/2 已由独立的原五列 Gram 排除。物理 D=0；本输入不移用 D 非零图的任何排除。

在 u=1 直接有
\[
P_{02}=(\ell-1)Q,\quad T_0=-\ell Q,\quad
J-Q=(\ell-1)Q,\quad P_f=\ell(1-\ell)Q^2,\quad
\Phi=(1-\ell)Q.
\]
所以本纤维的 ell-1、Pf 均从实际 P02 非零推出，无需旧整个 T0/JQ/Phi 定理。

## 2. 全自由 kappa 的原恢复

令
\[
\kappa=\frac{bc\,t}{\ell},\qquad
f=\lambda+h-\kappa,\qquad V=bX+cY=\lambda+\ell h,
\quad W_1=(T_0+4f)/2,\quad t=\frac{\ell\kappa}{bc}.
\]
原 P1、E0、N0 由这些式子恢复。取 m=1-ell、M=ell(2-ell Q)-1=4bc(1-Q)，
\[
x=\frac{(1-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-V}{M},\quad X=x+\rho y,\quad Y=x-\rho y.
\]
完整原 Gram 采用
\[
r=X-(1-\ell)p-ct,\quad s=Y-(1-\ell)q-bt,\quad
A_1=2f-2V+2bct.
\]
源码从真实 dual 乘法重新构造全部原 mean、N4、P2，首先在自由 kappa 上返回全部原 E0/N0/P0/P1 和谱矩。

令
\[
E(\lambda)=\lambda^2+\lambda-1.
\]
真原 V=(1,w,h,h) 的完整原身份是
\[
\boxed{\frac12N_4(V)=2E(\kappa-h)+\lambda h^2.}
\]
源直接以同一点完整 Gram 返回此式，不以错误 compact Rbad 或已剥参数多项式替代它。

## 3. 先处理全部斜率零纤维

有完全谱多项式恒等式
\[
Ah=A+B=\lambda(2\lambda-1)^2.
\]
因此 h 在本原图非零。若 E=0，原 N4(V)=0 便强制 lambda h^2=0，与实际原单位矛盾。这个论证处理 E=0 的全部复根，不是先倒 E 后遗漏其零点。

于是原点上恰可恢复
\[
\kappa_* =h-\frac{\lambda h^2}{2E},\quad
f=\lambda+\frac{\lambda h^2}{2E},\quad
A_1=\frac{(1-\ell)\lambda h^2}{E}.
\]
同一自由 kappa Gram 通过多项式求值 kappa→kappa_* 保持完整原身份。每个未排原点都在这张只剩自由 (lambda,Q) 的图上。

整个 h=k 的真 t=0 支此前已由原 mean/NP/矩与物理第五列排除，故 kappa_* 也是本纤维原单位；剥它的分子时只引用该独立真证明。没有倒 Delta、Nf、旧 compact cofactor 或任何新代数范数。

## 4. 固定原 Q 投影

同一点保留
\[
E_1,E_{B,e},E_{B,o},N_1,N_{B,e},N_{B,o},P_{B,e},P_{B,o}.
\]
偶、奇提取同时使用两个实际 B、C 原行和 rho 非零。所有分母逐项只允许 A、B、lambda、2lambda-1、E、ell-1、kappa_*、Q、1-Q、M 的实际原支持；源将每行清分母和全部仅已付因子剥除逐式乘回。

预定四个新目标为
\[
(E_1,E_{B,e}),\quad(E_1,E_{B,o}),\quad
(E_{B,e},E_{B,o}),\quad(E_{B,o},N_1)
\]
的固定实际 Q 次数 Sylvester 行列式。每一行是原多项式的真单项式倍；完整 Bareiss 整除返回。所有 Q 首项零、Delta=0 和原权交点都保留。若有一条原式本来不含 Q，则直接取这条原必要标量；绝不把两条零次多项式的空矩阵行列式误作1。

仅对最后纯 lambda 标量剥已付纯 lambda 支持，实际 QQ 累计 Bézout 乘回后若得到非零常数，才排除整个对称 u=1。若不是常数，就保留其全部 lambda 零纤维及自由 Q，不预设有限几何点。

## 5. 冻结源与唯一算术依赖

新源：2026-11-28-unit211-h-equals-k-symmetric-u-one-original-Q-projections-8542.py，10523 B，SHA256 59261a3fdb616fbb5f585017b0b2a195d453426d59e593d1acfd2db27d2ae43f。

唯一外部依赖是正确 f33 源 2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py，完整 SHA256 2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。本次只取 R 算术定义 1628 B / SHA256 208b244cf063707ca4613f8c61d8a351860639348961a77815d1f8fafd149765，与 U 算术定义 1127 B / SHA256 441ac944e389144cc94a7358f4fd1c011736d28f77daaf3edd4e15544aa0e3c9。没有执行旧参数恢复、旧五行、旧 cofactor 或其计时/资源设置。

根和独立同行均全文静核完成。实际状态以首次执行日志为准；只保存源、定义、次数/SHA与小回执，不保存可重算系数缓存。
