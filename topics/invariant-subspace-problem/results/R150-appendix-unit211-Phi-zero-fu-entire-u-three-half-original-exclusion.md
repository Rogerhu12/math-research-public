# R150 补充：正确 Phi 的 f=u 整 u=3/2 原分支排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 范围与结论

保持当前正确原 unit211 的
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0.
$$
本条证明
$$
\boxed{f=u\quad\Longrightarrow\quad u\ne3/2.}
\tag{1}
$$
这是 $f=u$ 子支的一条完整权纤维排除，不把 $2u-3$ 提升为整个 Phi 图的单位，也不声称整个 $f=u$ 或 Phi 已排空。

以下只用正确 dual 乘法、原 $E_0/N_0/P_1$ 恢复与两个 singleton 均值。由[正确整 t=0 排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)，当前物理图已有 $t\ne0$。不使用被撤回的旧 $R_{\rm bad}$、旧第一头单位或其有限性。

## 2. 整个 u=3/2 的原点恢复

反设 $f=u=3/2$。令
$$
\delta=1-Q,\quad P=2Q+1,\quad \rho^2=\delta.
$$
正确 Phi 权式及内在单位给
$$
\ell=\frac{P}{2Q},\qquad a=1-\ell=-\frac1{2Q},\qquad
bc=\frac{4Q+5}{16Q},
$$
$$
T_0=-Q-2,\qquad P_{02}=\frac P2,\qquad P_f=Q+2,
\tag{2}
$$
所以 $Q\delta P(4Q+5)(Q+2)\ne0$。

记 $V=bX+cY,\ v_n=QV,\ z=Qt$，以及
$$
n_n=Q(T_0+4uf)-2v_n.
$$
[正确 compact 原身份](../notes/2026-11-28-unit211-corrected-dual-germ-compact-original-identities-8542.js)中的
$$
R=4Q(f-u)(v_n-Qf)+bc z^2
  +z(4bcuQ-\ell v_n)
  +\frac{u-\ell}{2\delta}zn_n
\tag{3}
$$
满足 $2R+Q^2(E_1-bE_B-cE_C)=0$。这里使用的是真 $E_1-bE_B-cE_C$，不是把 $R$ 误作 $E_1$ 本身。

在 $f=u$ 时，原 $E_0/N_0$ 给
$$
v_n=v_0+bc z,\qquad
v_0=(2u-1)Q-4(u-1)^3-\lambda P_{02}.
$$
代入 (3)，在 (2) 上直接得到
$$
\frac Rz=\frac{4(2Q+1)\lambda-2Q+5}{8}.
\tag{4}
$$
原点上 $R=0$，且 $z=Qt\ne0$，故
$$
\lambda=\frac{2Q-5}{4(2Q+1)}.
\tag{5}
$$
没有删除任何 $\lambda$ 首项零纤维：本式唯一的权分母 $P$ 已由 $P_{02}\ne0$ 支付。

原 $P_1$ 为
$$
P_f f+bcQ\Phi t+QP_{02}(\ell+T)
-\bigl[\lambda P_{02}-(1-u)T_0\bigr]T_0=0.
$$
利用 (2)、(5) 得
$$
T=-\frac34,\qquad A_1=-\frac{2Q+1}{4Q}.
\tag{6}
$$
完整两均值恢复为
$$
X=\frac32+\frac t4+
 \rho\,\frac{10-4Q-3t}{8(1-Q)},\qquad
Y=\frac32+\frac t4-
 \rho\,\frac{10-4Q-3t}{8(1-Q)},
\tag{7}
$$
$$
b=\frac{2Q+1-\rho}{4Q},\qquad
c=\frac{2Q+1+\rho}{4Q},\qquad
p=1+\rho,\quad q=1-\rho.
$$
这同时保留 $\rho$ 的两种选择。令
$$
r=X-ap-ct,\qquad s=Y-aq-bt.
$$
同一原 Gram 的四行是
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad g_C=(q,s,t,0).
\tag{8}
$$

## 3. 两个原 singleton 均值的短返回

原乘法与迹为
$$
v\,w=(v_0w_0,\ v_0w_1+v_1w_0,\ v_Bw_B,\ v_Cw_C),
\qquad
\tau(v)=av_0+v_1+bv_B+cv_C.
$$
置 $d=K1=(u,d_1,X,Y)$。由 (2)、(6)–(8)，
$$
d_1=\frac{5(2Q+1)}{8Q}-bc\,t,\qquad \tau(d)=2u=3.
$$
原 singleton 均值直接展开为
$$
E_B=-ap^2+(2p+3)X-2pd_1
 +ct(t+3-2p-2Y)-2X^2,
\tag{9}
$$
$E_C$ 为其 $\rho\mapsto-\rho$ 共轭。写
$$
E_B=E_{\rm e}+\rho E_{\rm o},\qquad
E_C=E_{\rm e}-\rho E_{\rm o}.
$$
把 (7) 代入 (9)，逐项收取 $\rho$ 系数即得
$$
\boxed{E_{\rm o}
=-\frac{(2Q+1)(t-2)^2}{16Q(1-Q)}.}
\tag{10}
$$
这里仅以原单位 $Q(1-Q)(2Q+1)$ 为分母。于是原复点 $E_{\rm o}=0$ 必有 $t=2$。

在 $t=2$ 时，
$$
X=2+\rho/2,\qquad Y=2-\rho/2,\qquad d_1=3/4.
$$
再取 (9) 的偶部得到
$$
\boxed{E_{\rm e}\big|_{t=2}=-Q/2.}
\tag{11}
$$
这与 $E_{\rm e}=0$ 及 $Q\ne0$ 矛盾，完成 (1)。

(10) 中出现平方不造成遗漏：本条排的是全部复原点；相应均值理想含 $(t-2)^2$，而 (11) 也说明其在 $Q\ne0$ 环上的商没有复点。证明没有倒置原物理 $D$ 或它的范数。

## 4. 已完成的独立 exact 原返回

与上面的纸面短证配套，[冻结源](../notes/2026-11-28-unit211-Phi-zero-fu-u-three-half-original-return-8542.js)在 pure V8 BigInt 中实际正常返回，耗时 72 ms。其 SHA256 为
`d5e620d83fe6d682f2b02b4aa19b18f72e5860e8dd725d4314b747dd5e682199`。

源从 (8) 的真实乘法直接构造原均值、原 $N_1$ 与完整 weighted $NS/PS$，返回 $E_0,N_0,P_1$、真实 $E_1=bE_B+cE_C$ 和共轭等原身份。它另以固定 $t$ 次数 $(2,2)$ 的两个四阶原 Sylvester，分别对 $(N_1,E_{\rm e})$、$(N_1,E_{\rm o})$ 得到 $Q$ 次数 12、8 的真实 QQ 投影，并以完整 QQ Bézout 乘回得到
$$
\gcd(R_{N_1,E_{\rm e}},R_{N_1,E_{\rm o}})
=Q^2(1-Q)^2.
$$
仅剥这两个已付原单位后余常数 1。固定 Sylvester 保留了所有 $Q$ 处的 $t$ 首项退化，没有泛型次数代替固定矩阵。

实际计数为 5659 次整数多项式乘法、379 次完整整数除法乘回、12 项原检查，以及 28 次固定 Sylvester 完整精除。原 $NS/PS$ 在该源内已构造，但终端排除在前两个投影后即完成。源未另执行 (10)–(11) 的特定打印或断言；这两个显示式是上节由 (9) 给出的纸面短证。没有为登记该结论再加整源回放。

[小回执](../notes/2026-11-28-unit211-Phi-zero-fu-u-three-half-original-return-8542-execution.json)保留实际正常返回、完整小统计与范围。当前仍需继续 $f=u,\ u\ne3/2$ 以及其余正确 Phi 原支。
