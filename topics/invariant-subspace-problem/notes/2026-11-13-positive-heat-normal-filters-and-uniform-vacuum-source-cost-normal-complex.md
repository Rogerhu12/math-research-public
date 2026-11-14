# 工作补充：正热过滤的正常泛函、有限头检测与统一真空源成本

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro；根全文核验，central_review 独审 §§2–4。

状态：以下为既有 R240 正热弱闭包的正常泛函应用与一个明确的有限头检测预算。正热算子球的弱闭包、任意正热预算逃逸、规范头源的自适应负权发散，均已由并发主线发表，本稿不重新计作这些结论。

本稿的新接口是：固定一个非零真正常湮灭泛函，在整个有界正 $\ell^2$ 热预算球内过滤后，其弱闭包仍是一个不含零的弱紧正常泛函族；因此，这整个变化泛函族的固定真空近似源成本一致趋于无穷。对于正密度，给出真实有限头右因子、其范数及一个有限测试网的具体预算。没有更换原正见证，没有对未知商的正交投影假设保权。

## 1. 已发表输入与准确记号

保持原 Haar 空间 $H$、真空 $\Omega$、实际交换子
$$
\mathfrak C=A',\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\qquad
\Phi_u(F)=\langle Fu,\Omega\rangle.
\tag{1.1}
$$
内积第一变量线性，原 $\Omega$ 对 $A$ 及 $A^*$ 均循环。
有限 Walsh 乘子满足
$$
V_F\Omega=\chi_F,\qquad
C\chi_F=(-1)^{|F|}\chi_F,\qquad
\|V_j\|\le3.
\tag{1.2}
$$

对 $b\in\ell^2_+$，记实际正 first 热算子
$$
R(b)=e^{-X_b}\in\mathfrak C,\qquad \|R(b)\|\le1.
\tag{1.3}
$$
它与每个 $\mathfrak C$ 元素交换；这使用实际强多项式闭包，不把纯尾算子放入 $\mathfrak C$。

以下三个输入已经发表。

1. [R240 完整正热弱闭包](../results/R240-appendix-complete-weak-closure-of-positive-heat-families.md) §4 给
   $$
   \mathscr K_B:=
   \overline{\{R(b):b\ge0,\ \|b\|_2\le B\}}^{\mathrm{WOT}}
   =
   \left\{\lambda R(b):
   \|b\|_2^2-2\log\lambda\le B^2,\quad
   b\ge0,\quad0<\lambda\le1\right\}.
   \tag{1.4}
   $$
   特别 $\lambda\ge e^{-B^2/2}>0$。
   该稿已经完整支付真实头与纯尾的算子范数误差、全部有限柱配对、标量范围及 flat 尾块端点。此处不重证该闭包。

2. [R150 准确热旗与闭图](../results/R150-appendix-exact-heat-ranges-on-invariant-flags-and-closed-graphs.md) §2 给同一组真实强单位
   $$
   D_m(b)=\exp\!\left(\sum_{j<m}b_jV_j\right)\in\mathcal A,\qquad
   R(b)D_m(b)=R(b\mathbf1_{j\ge m}),
   $$
   $$
   \|R(b)D_m(b)\|\le1,\qquad
   R(b)D_m(b)\longrightarrow I\quad\mathrm{SOT}.
   \tag{1.5}
   $$
   这里 $b$ 固定。$D_m(b)$ 不要求在 $m$ 上一致有界。

3. [R150 实际正常矩负权判据](../results/R150-appendix-actual-normal-moments-negative-occupation-criterion-and-witness-divergence.md) §8 已证明：对于真非零正常湮灭者，规范完整矩头、有限头代表及指定实际擦除源，在任何有界正 $\ell^2$ 自适应负权预算下都发散。以下不把同一源发散改名为新结论。

记正常泛函在 $\mathfrak C$ 上的范数为 $\|\cdot\|_{\mathfrak C_*}$，即对 $\mathfrak C$ 单位球取上确界。

## 2. 热过滤正常泛函的准确弱闭包

固定一个迹类正常泛函 $\phi$，并定义
$$
\psi_b(F)=\phi(R(b)F)\qquad(F\in\mathfrak C).
\tag{2.1}
$$
即使原 $\phi$ 为正，$\psi_b$ 也未必为正。本稿不把它写成未经证明的正密度 $R(b)\rho R(b)^*$。

由于 $\|R(b)\|\le1$，
$$
\|\psi_b\|_{\mathfrak C_*}\le\|\phi\|.
\tag{2.2}
$$
对固定 $F\in\mathfrak C$，$T\mapsto\phi(TF)$ 是一个正常泛函。
在有界算子球上，WOT 收敛使每个这样的正常配对收敛：
先用有限秩迹类逼近 $\phi(\,\cdot\,F)$，再用统一算子范数控制尾差即可。
因此
$$
T\longmapsto[F\mapsto\phi(TF)]
\tag{2.3}
$$
从有界 WOT 集到正常泛函的弱拓扑 $\sigma(\mathfrak C_*,\mathfrak C)$ 连续。

对 (1.4) 应用 (2.3)，得到准确的弱紧闭包
$$
\boxed{
\overline{\{\psi_b:b\ge0,\ \|b\|_2\le B\}}^{\,w}
=
\left\{\lambda\psi_b:
b\ge0,\quad0<\lambda\le1,\quad
\|b\|_2^2-2\log\lambda\le B^2\right\}.
}
\tag{2.4}
$$
说明闭包相等时，只需注意：连续像包含原族的全部弱极限，而 (1.4) 中每个点均由原热族收敛到它，故其正常泛函像也属于闭包。像为弱紧集，因而闭。

若 $\phi|_{\mathfrak C}\ne0$，则每个 $\psi_b\ne0$。
否则 (1.5) 给，对每个固定 $F\in\mathfrak C$，
$$
0=\psi_b(D_m(b)F)
=\phi(R(b)D_m(b)F)
\longrightarrow\phi(F),
$$
与非零性矛盾。
结合 $\lambda>0$，(2.4) 的整个弱紧集都不含零。

特别存在有限个实际右测试 $F_1,\ldots,F_N\in\mathfrak C$ 及 $\epsilon_B>0$，使
$$
\max_{1\le i\le N}|\psi_b(F_i)|\ge\epsilon_B
\qquad(b\ge0,\ \|b\|_2\le B).
\tag{2.5}
$$
这是弱紧集与零点的有限坐标分离；不要求这些泛函组成凸集，也不声称存在一个共同单测试。
下一节在原 $\phi$ 为正时，直接构造这样的有限头测试网并付其范数。

## 3. 正密度下的明确有限头检测

现在设 $\phi=\varphi_\rho$，$\rho\ge0$、$\tau=\operatorname{Tr}\rho>0$。
令 $\Pi_m$ 为前 $m$ 位 Walsh 柱投影，置
$$
\delta_m=\operatorname{Tr}\rho(I-\Pi_m)\longrightarrow0,\qquad
r_B=e^{-B^2/2}.
\tag{3.1}
$$
给定 $b\ge0$、$\|b\|_2\le B$，实际右因子 $D_m(b)$ 满足
$$
\boxed{\|D_m(b)\|\le E_{B,m}:=e^{3B\sqrt m}.}
\tag{3.2}
$$
因为 $\sum_{j<m}b_j\le B\sqrt m$。

从真实尾与纯尾的有界 Duhamel 预算，
$$
\|R(b_{\ge m})-R^0(b_{\ge m})\|
\le8B\|\eta_{\ge m}\|_2.
\tag{3.3}
$$
纯尾在头柱压缩上准确为一个正标量：
$$
\Pi_mR^0(b_{\ge m})\Pi_m=r_m(b)\Pi_m,
$$
$$
r_m(b)=\prod_{j\ge m}e^{-b_j}(1+b_j)
=\exp\!\left[-\sum_{j\ge m}(b_j-\log(1+b_j))\right]
\ge r_B.
\tag{3.4}
$$
这里使用 $0\le x-\log(1+x)\le x^2/2$。

正密度的双侧截断误差准确可估为
$$
\|\rho-\Pi_m\rho\Pi_m\|_1
\le\delta_m+2\sqrt{(\tau-\delta_m)\delta_m}.
\tag{3.5}
$$
例如把 $\rho$ 写成正平方分解后，对两个交叉块使用 Hilbert--Schmidt Cauchy--Schwarz。
因此 (1.5)、(3.3)--(3.5) 给
$$
\begin{aligned}
\operatorname{Re}\psi_b(D_m(b))
&=\operatorname{Re}\varphi_\rho(R(b_{\ge m}))\\
&\ge r_m(b)(\tau-\delta_m)
-\delta_m-2\sqrt{(\tau-\delta_m)\delta_m}
-8B\tau\|\eta_{\ge m}\|_2.
\end{aligned}
\tag{3.6}
$$

选择一个固定 $m\ge1$，使
$$
\delta_m\le\frac{\tau r_B^2}{256},\qquad
8B\|\eta_{\ge m}\|_2\le\frac{r_B}{8}.
\tag{3.7}
$$
正常性与实际 carry 衰减保证这样的 $m$ 存在。
它可以依赖当前同一个 $\rho$ 与 $B$，但不依赖球内后续选择的 $b$。
因为 $r_B\le1$，(3.6) 于是给
$$
\boxed{
\operatorname{Re}\psi_b(D_m(b))\ge\frac{\tau r_B}{2}.
}
\tag{3.8}
$$
从而有明确的正常泛函范数下界
$$
\boxed{
\inf_{\substack{b\ge0\\\|b\|_2\le B}}
\|\psi_b\|_{\mathfrak C_*}
\ge\frac{\tau}{2}
\exp\!\left(-\frac{B^2}{2}-3B\sqrt m\right)>0.
}
\tag{3.9}
$$

### 3.1 有限个固定的实际右测试

(3.8) 的右因子随 $b$ 变化，但只依前 $m$ 个坐标。
对正欧氏球
$$
K_{B,m}=\{x\in[0,\infty)^m:\|x\|_2\le B\}
$$
置 $D(x)=\exp(\sum_{j<m}x_jV_j)$。
有界指数的 Duhamel 恒等式给
$$
\|D(x)-D(y)\|
\le3\sqrt m\,E_{B,m}\|x-y\|_2.
\tag{3.10}
$$
可在 $K_{B,m}$ 内选一个半径
$$
u=\frac{r_B}{12\sqrt m\,E_{B,m}}
\tag{3.11}
$$
的有限欧氏网 $x^{(1)},\ldots,x^{(N)}$，并可取
$$
N\le(1+2B/u)^m.
\tag{3.12}
$$
令 $F_i=D(x^{(i)})\in\mathcal A$，均满足 $\|F_i\|\le E_{B,m}$。
给每个 $b$ 选网点逼近 $b_{<m}$，则 (3.10) 的算子差至多 $r_B/4$。
由 $\|\psi_b\|\le\tau$ 与 (3.8)，得到
$$
\boxed{
\max_{1\le i\le N}\operatorname{Re}\psi_b(F_i)
\ge\frac{\tau r_B}{4}
\qquad(b\ge0,\ \|b\|_2\le B).
}
\tag{3.13}
$$
全部 $F_i$ 都是同一个有限实际头的有界 $\mathcal A$ 元素，保留其对无限尾的真实 carry。
没有用纯尾算子本身作理想测试。

## 4. 整个热过滤族的一致近似源成本

设 $Z\in\mathcal A$ 在原 $H$ 上单射，且
$$
\phi|_{\mathfrak C}\ne0,\qquad
\phi(ZF)=0\quad(F\in\mathfrak C).
\tag{4.1}
$$
热算子与 $Z$ 交换，所以同一原泛函的全部过滤都满足
$$
\psi_b(ZF)=0.
\tag{4.2}
$$

定义
$$
c_B(\epsilon)=
\inf\left\{\|u\|:
u\in H,\quad
\exists b\ge0,\ \|b\|_2\le B,\quad
\|\Phi_u-\psi_b\|_{\mathfrak C_*}\le\epsilon
\right\}.
\tag{4.3}
$$
空集时取 $+\infty$。

**命题4.1。**
$$
\boxed{c_B(\epsilon)\longrightarrow\infty
\quad\text{当 }\epsilon\downarrow0.}
\tag{4.4}
$$

若不成立，选 $\epsilon_n\downarrow0$、$\|u_n\|\le K$ 及球内 $b_n$ 使 (4.3) 成立。
下确界未取到时先将统一范数界增加 $1$，再取满足约束的实际源。
取子列 $u_n\rightharpoonup u$。
由 (2.4) 的弱紧性，再取子列使
$$
\psi_{b_n}\rightharpoonup\lambda\psi_b,\qquad
\lambda>0.
$$
于是对每个固定 $F\in\mathfrak C$，
$$
\Phi_u(F)=\lambda\psi_b(F).
\tag{4.5}
$$
右侧非零。
另一方面，(4.2) 给 $\Phi_u(ZF)=0$。
取 $F=A^k$，利用 $Z$ 与 $A$ 交换及 $\Omega$ 对 $A^*$ 的循环性，
得到 $Zu=0$。
单射性使 $u=0$，与 (4.5) 非零矛盾。

这是对所有变化 $b$ 和所有近似源 $u$ 的一致结论，不只针对某一个预先给定的源序列。
没有给 $c_B$ 的发散速度，也不是最小秩删除一个原源所用的 $C_i(\epsilon)$。

### 4.1 已有实际源的准确接入与旧结论扣除

对 $\rho\ge0$，R230 [正密度截断稿](../results/R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md) §4.1 已构造明确的 $h_p\in H$，满足
$$
\|\Phi_{h_p}-\varphi_\rho\|_{\mathfrak C_*}=\delta_p\to0,
\qquad
\|h_p\|\le2\tau10^{p/2}.
\tag{4.6}
$$
由于 $R(b)$ 收缩且属于实际交换子，
$$
\|\Phi_{R(b)h_p}-\psi_b\|_{\mathfrak C_*}\le\delta_p.
\tag{4.7}
$$
因此每个正误差下 (4.3) 都有实际近似源，且
$$
\inf_{\substack{b\ge0\\\|b\|_2\le B}}\|R(b)h_p\|
\ge c_B(\delta_p)\longrightarrow\infty.
\tag{4.8}
$$
当某个 $\delta_p=0$ 时，(4.6) 本身已给与 (4.1) 矛盾的准确源；真见证下这种情形不会发生。

由 R150 准确热范数在 $\ell^2$ 球上的统一比较，
$$
M_B^{-1}\|e^{-2\mathcal N_b}h\|
\le\|R(b)h\|\le
M_B\|e^{-2\mathcal N_b}h\|,
\tag{4.9}
$$
(4.8) 同样给 $h_p$ 的统一负权发散。
然而，这个特定序列的负权结论也可直接从已发表 R150 全矩判据推出：
$\Phi_{h_p}(V_F)\to\phi(V_F)$，若存在有界加权子列，就取 $b_p$ 的弱极限，对每个固定有限头取极限，再用完整加权矩判据。
因此 (4.8)--(4.9) 只作为 (4.4) 的实际应用记录，不独立宣称新的负权障碍。

## 5. 同一个联合二次核见证与仍缺的上界

[R236 迟首二次核的联合正见证](../results/R236-appendix-late-support-quadratic-kernels-and-positive-joint-first-annihilators.md)
从假想非零核产生一个固定 $\rho=h\otimes h$，以及一个已经选定的 $\zeta$，使同一 $\phi=\varphi_\rho$ 满足
$$
\phi(S_\zeta F)=\phi(TF)
=\phi((Y-B_0+H_\zeta^2)F)=0
\quad(F\in\mathfrak C),
\tag{5.1}
$$
其中 $S_\zeta=X+H_\zeta$ 在全空间单射。

本稿可取 $Z=S_\zeta$。
每个 $\psi_b$ 仍准确满足全部三条式子，因为只是插入同一个实际右因子 $R(b)$。
不从中产生新的正密度，也不改变 $\zeta$ 或见证 $h$。
在任意有界热预算球内，§3 的有限测试保留非零正常泛函，而 §4 迫整个族的实际近真空源成本一致发散。

还没有以下充分上界：
由第二条慢行或原核关系，构造球内 $b_n$ 与有界 $u_n$，使
$$
\|\Phi_{u_n}-\varphi_\rho(R(b_n)\,\cdot)\|_{\mathfrak C_*}\to0.
\tag{5.2}
$$
一旦能从真联合结构推出 (5.2)，就会与 (4.4) 矛盾；当前没有这样的构造。
(4.6) 的上界仍随 $p$ 增长，正常尾 $\delta_p$ 没有未证速度。

准确加权商只给某个加权代表，未证明原正交代表 $h\in M\ominus N$ 获得 ambient 占据权。
商上的快因子逆也未被提升为 $M$ 上的同一逆。
因此本稿不通过正交投影、左 UHF 反射或换见证取消这些源费用。
一般正常湮灭者和普通 Hilbert ISP 仍未关闭。
