# 全部 p-neighbors 的实际单位范数、固定 κ 单位与完整 cochain

日期：2026-11-12。状态：同源范数、全部 $p+1$ 个邻点的乘积、
$\kappa_{[p],P}$ 的准确除法函数公式、固定单位 Frobenius 商、
原 $\mathcal S-i\mathcal S^{\rm rot}$ 投影和 cochain 换位项均已证明。
它们没有证明中央导数在无穷多个素数上非零。
特别，本文准确分开沿纤维为常数的 $\log\kappa$ 与正垂直 jet。

## 1. 固定原单位和参考除子

使用[实际除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)：
\[
 E_\lambda:y^2=x(x-1)(x-\lambda),\quad
 \omega=\frac{dx}{2y},\quad D=d/\omega,\quad Z=-x/y,\quad N=68.
\]
$\Psi_n$ 采用与不变微分相容的 sigma 规范
\[
 \Psi_n(z)=\frac{\sigma(nz)}{\sigma(z)^{n^2}},
 \qquad \Psi_n(z)=n z^{1-n^2}+\cdots \quad(z\to0).
 \tag{1}
\]
它是有理除法函数。对于非零 $N$ 挠点 $P$，记
\[
 d_P=D\Psi_N(P),\qquad
 r_P(R)=\frac{\Psi_N(P+R)}{d_P Z(R)}.
 \tag{2}
\]
$r_P(O)=1$。完整除子为
\[
 \operatorname{div}r_P=D_N-N^2(-P),\qquad
 D_N=\sum_{R\in E[N]\setminus O}(R)-T_0+T_1+T_\lambda.
 \tag{3}
\]
所以 $\deg D_N=N^2$。其中 $T_0$ 的系数为零，
$T_1,T_\lambda$ 的系数为二；本文从不丢掉这些参考点修正。
固定整模型保证所有 $d_P$ 在 $p\nmid2N$ 的光滑邻域为单位。

$\mathcal S$、$\mathcal S^{\rm rot}$ 仍是原来的两个 $256$ 点轨道。
各同源下必须运输这些全部标签以及三个二挠点，不能另取一组
方便的 level 标签代替原来的有限角色。

## 2. 任意奇次数同源的准确常数

令 $\varphi:E\to E'$ 为奇次数 $n$ 的可分同源，
$(n,N)=1$，并把 $N$ 级及二级标签经 $\varphi$ 送到 $E'$。
在必要的有限扩域上取与这些标签相容的 Legendre 模型；
$r'_{\varphi P}$ 按 (2) 在该模型上定义。

$\varphi$ 在 $E[N]$ 上是双射，且
$\varphi_*D_N=D_N'$。故
\[
 \operatorname{div}(\operatorname{Norm}_\varphi r_P)
     =D_N'-N^2(-\varphi P)
     =\operatorname{div}r'_{\varphi P}.
\]
在 $O'$ 取值，准确得到
\[
 \boxed{\quad
 \operatorname{Norm}_\varphi r_P
      =\kappa_{\varphi,P}r'_{\varphi P},\qquad
 \kappa_{\varphi,P}=\prod_{Q\in\ker\varphi}r_P(Q).
 \quad}
 \tag{4}
\]
所有因子都可取值：$\ker\varphi$ 与 (3) 的支撑不交；
$Q=O$ 的因子准确为一。

令 $\Psi_\varphi$ 为任何满足
\[
 \operatorname{div}\Psi_\varphi
     =\sum_{Q\in\ker\varphi\setminus O}(Q)-(n-1)(O)
\]
的函数。因 $n$ 为奇数，核中点成 $\pm Q$ 对，故这个除子是 principal；
$\Psi_\varphi$ 也是偶函数。Weil reciprocity 的支撑在此完全不交，
所以
\[
 \boxed{\quad
 \kappa_{\varphi,P}
 =\frac{K_{\varphi,N}}{\Psi_\varphi(P)^{N^2}},
 \qquad
 K_{\varphi,N}
   =\prod_{R\in\operatorname{supp}D_N}
                  \Psi_\varphi(R)^{D_N(R)} .
 \quad}
 \tag{5}
\]
这是完整常数式。将 $\Psi_\varphi$ 乘以一个常数，
(5) 的分子、分母都乘同一 $N^2$ 次幂，完全相消。

这里所需 reciprocity 可直接由函数范数证明：
对支撑不交的 $f,g$，沿 $f:C\to\mathbb P^1$ 取 $g$ 的范数。
它在 $0,\infty$ 的值之比是 $g(\operatorname{div}f)$；
而在 $\mathbb P^1$ 写其零极点乘积，
同一个比值是 $f(\operatorname{div}g)$。
这也核定了 (5) 的方向，没有把它倒置。

## 3. 全部 p+1 个 cyclic neighbors 的 κ 恰乘成 [p] 的 κ

现在取奇素数 $p\nmid N$，在特征零工作。
令 $G$ 跑遍 $E[p]$ 的 $p+1$ 个阶 $p$ 子群，
$\varphi_G:E\to E/G$ 为商同源。$E[p]\setminus O$ 被
这些 $G\setminus O$ 不相交地分拆。
因为 $r_P(O)=1$，(4) 立即给
\[
 \boxed{\qquad
 \prod_G\kappa_{\varphi_G,P}=\kappa_{[p],P}.
 \qquad}
 \tag{6}
\]
这里 $[p]$ 的次数是 $p^2$，而单个 neighbor 的次数是 $p$；
没有将两种范数混用。

更强的、在整个源椭圆曲线上成立的归一函数恒等式为
\[
 \boxed{\quad
 \prod_G r^{E/G}_{\varphi_GP}(\varphi_G R)
       =r_P(R)^p\,r_{pP}([p]R).
 \quad}
 \tag{7}
\]
证明：拉回 (4)，左侧未除常数时为
$\prod_G\prod_{Q\in G}r_P(R+Q)$。
非零 $p$ 挠点各出现一次，$O$ 出现 $p+1$ 次，
所以它等于
\[
 r_P(R)^p\prod_{Q\in E[p]}r_P(R+Q).
\]
再使用 $[p]$ 的 (4) 和 (6)，得到 (7)。

(7) 保留全部阶数的 germ，而不仅是一个 first-jet Hecke 关系。
若 $\varphi_G^*\omega_G=c_G\omega$，在加法局部参数中准确有
\[
 \sum_G c_G^k
    D_G^k\log r^{E/G}_{\varphi_GP}(O)
 =
 p\,D^k\log r_P(O)+p^kD^k\log r_{pP}(O)
 \quad(k\ge1).
 \tag{8}
\]

## 4. κ_[p],P 的完全规范：所有 p 因子都可核查

对 $[p]$，(5) 中的 $\Psi_\varphi$ 可取 (1) 的 $\Psi_p$。
定义
\[
 K_{p,N}=\prod_R\Psi_p(R)^{D_N(R)}.
\]
于是
\[
 \kappa_{[p],P}=\frac{K_{p,N}}{\Psi_p(P)^{N^2}}.
 \tag{9}
\]

还可将每个 $\Psi_p(P)$ 精确换成固定 $N$ 除法函数的导数。
sigma 定义直接给 composition 恒等式
\[
 \Psi_N([p]R)\Psi_p(R)^{N^2}
       =\Psi_p([N]R)\Psi_N(R)^{p^2}.
 \tag{10}
\]
在 $R=P+z$ 处比较一次项。
左侧一次项为
$p\,d_{pP}\Psi_p(P)^{N^2}z$；
右侧由 $\Psi_p(Nz)=p(Nz)^{1-p^2}+\cdots$ 得
$pN^{1-p^2}d_P^{p^2}z$。
两侧的 $p$ 准确相消，故
\[
 \boxed{\quad
 d_{pP}\Psi_p(P)^{N^2}=N^{1-p^2}d_P^{p^2},
 \quad
 \kappa_{[p],P}
  =K_{p,N}N^{p^2-1}\frac{d_{pP}}{d_P^{p^2}} .
 \quad}
 \tag{11}
\]
所以在此规范中，不能再补一个未经推导的 $p/\Psi_p(P)$ 因子。
(9) 和 (11) 已给未取幂的准确常数；不需要猜 division resultant 的符号。

令
\[
 \mathcal D=\prod_R d_R^{D_N(R)},\qquad
 w_P=\frac{d_P^{N^2}}{\mathcal D}.
 \tag{12}
\]
这些是固定 $68$ 级覆盖上的真实代数单位，均保留 (3) 的参考除子。
将 (11) 的第一个等式按 $D_N$ 加权相乘。
因为奇数 $p$ 逐点保持三个二挠点，并置换其余 $N$ 挠点，
得到
\[
 K_{p,N}^{N^2}
   =N^{-N^2(p^2-1)}\mathcal D^{p^2-1}.
\]
代入 (11)，即得无需选择任何根的恒等式
\[
 \boxed{\quad
 \kappa_{[p],P}^{N^2}
     =\frac{w_{pP}}{w_P^{p^2}}.
 \quad}
 \tag{13}
\]
这里所有 $w_R$ 都来自同一个固定有限集合；没有用随 $p$
增加的代数数集合代替固定性。

## 5. 原 256 点、CM 共轭与固定 Frobenius 商

$\mathcal S$ 的 scalar 生成元 $-3$ 在
$(\mathbb Z/68)^\times$ 中生成全部 $u\equiv1\pmod4$ 的元素。
确实该子群有 $16$ 个元素，且 $-3$ 模 $17$ 的阶为 $16$。
所以令 $\epsilon_p=(-1/p)$，便有
\[
 p\mathcal S=\epsilon_p\mathcal S,\qquad
 p\mathcal S^{\rm rot}=\epsilon_p\mathcal S^{\rm rot}.
 \tag{14}
\]
由于 $N$ 为偶数，$\Psi_N$ 为奇函数、$d_{-P}=d_P$，
并且从 (2) 直接得到
\[
 \boxed{\qquad r_{-P}(R)=r_P(-R).\qquad}
 \tag{15}
\]
本式在实际 Legendre 参考 $Z=-x/y$ 中准确成立，
不需要额外常数。

定义
\[
 d_{\mathcal S}=\prod_{P\in\mathcal S}d_P,\qquad
 w_{\mathcal S}=\prod_{P\in\mathcal S}w_P
       =\frac{d_{\mathcal S}^{N^2}}{\mathcal D^{256}},
 \qquad
 \kappa_{p,\mathcal S}=\prod_{P\in\mathcal S}\kappa_{[p],P}.
 \tag{16}
\]
则 (13)–(15) 给
\[
 \boxed{\quad
 \kappa_{p,\mathcal S}^{N^2}
        =w_{\mathcal S}^{\,1-p^2},
 \qquad
 \kappa_{p,\rm rot}^{N^2}
        =w_{\rm rot}^{\,1-p^2}.
 \quad}
 \tag{17}
\]
这是真正固定单位的幂公式。若改记
$W_{\mathcal S}=w_{\mathcal S}^{-1}$，
则等价于
$\kappa_{p,\mathcal S}^{N^2}=W_{\mathcal S}^{p^2-1}$。

进一步在实际 CM 纤维 $\lambda=1/2$ 专门化。
对每个惰性 $p\ge7$，其 trace 为零，约化曲线上的 $p$ 次幂 Frobenius 自同源满足
$\pi_p^2=[-p]$。$N$ 挠点处于未分歧扩域，约化映射单射；
故算术 Witt Frobenius 的平方准确满足
\[
 \sigma_p^2(R)=[-p]R\qquad(R\in E[N]).
\]
由于 $d_{-R}=d_R$、$[-p]_*D_N=D_N$，(13) 成为
\[
 \boxed{\quad
 \kappa_{[p],P}^{N^2}
       =\frac{\sigma_p^2(w_P)}{w_P^{p^2}},
 \qquad
 \kappa_{p,\mathcal S}^{N^2}
       =\frac{\sigma_p^2(w_{\mathcal S})}
              {w_{\mathcal S}^{p^2}},
 \quad \sigma_p^2(w_{\mathcal S})=w_{\mathcal S}.
 \quad}
 \tag{18}
\]
这只是本篇实际 norm 所对应的固定单位；
没有因此把全范数同原来指定的局部 tame 角色系数等同。

实际偶投影的常数对数为
\[
 L_{\kappa,e}
 =-\frac{c_e}{2N^2}
        \{\log\kappa_{p,\mathcal S}
                       -i\log\kappa_{p,\rm rot}\}.
\]
在目标素数处取通常的 $p$-adic 单位对数，
由 (17) 准确得到
\[
 \boxed{\quad
 L_{\kappa,e}
   =\frac{c_e(p^2-1)}{2N^4}
         \{\log w_{\mathcal S}-i\log w_{\rm rot}\}.
 \quad}
 \tag{19}
\]
并没有把 $i$ 当作 $\sigma_p$ 固定的数。

在 CM 纤维，$\iota^*\omega=i\omega$，且 sigma 规范给
\[
 \Psi_N(\iota R)=i^{1-N^2}\Psi_N(R),\qquad
 d_{\iota R}=i^{-N^2}d_R=d_R.
\]
因此 $d_{\rm rot}=d_{\mathcal S}$、
$w_{\rm rot}=w_{\mathcal S}$，(19) 简化为
\[
 L_{\kappa,e}
   =\frac{c_e(1-i)(p^2-1)}{2N^4}\log w_{\mathcal S}.
 \tag{20}
\]
这不要求错误的全局式 $Z(\iota R)=iZ(R)$：
在 Legendre 模型上该式并不成立。
这里只使用了 $d_R$ 的准确 CM 权和两组点的旋转关系，
共同的 $\mathcal D$ 自始至终都保留。

若将来证明 $w_{\mathcal S}$ 非根单位，(20) 的单位对数在每个目标
$p$ 都非零；本文没有把这个条件当成已证，也没有把 (20)
当作中央 Sha 导数。

## 6. 完整归一 germ 与 inert first-jet trace

将 (7) 对 $\mathcal S$ 以及旋转轨道分别相乘，再取实际线性组合。
令 $h_{e,G}$ 在 $E/G$ 上使用运输后的原标签与同一个 $c_e$。
所有对数在 $R=O$ 规范为零，则
\[
 \boxed{\quad
 \sum_G h_{e,G}(\varphi_G R)
       =p h_e(R)+h_e(\epsilon_p[p]R).
 \quad}
 \tag{21}
\]
因此在加法局部参数中，对每个 $k\ge1$，
\[
 \sum_G c_G^kD_G^kh_{e,G}(O)
       =(p+\epsilon_p^kp^k)D^kh_e(O).
 \tag{22}
\]
惰性处 $k=1$ 的右侧准确为零。
这与实际权一 first-jet 的 inert Hecke trace 相容；
但 (21) 自己没有把运输后的 GSp 标签偷偷换回一个固定
symplectic 分量。若要用标准 $T_p,U_p$ 记号，
还必须保留相应 diamond/有限角色的作用。

(22) 同时显示其高垂直阶不是全部为零：
惰性处奇数 $k>1$ 的因子是 $p-p^k$，
偶数 $k$ 的因子是 $p+p^k$。
所以只保留 $k=1$ 的 trace 会丢失完整 germ 的信息。

## 7. 作用于完整 Frobenius cochain 时的精确换位项

为不假设一个不存在的 integral Frobenius–isogeny commuting square，
先在特征零的共同正式域中写恒等式。
若 $u(t,Z)$ 在 $Z=0$ 为一，取源上的正式 lift
$\Phi_E(t,Z)=(t^p,F_E(t,Z))$，并定义
\[
 \mathcal B_{\Phi_E}(u)
   =\frac1p\{\log(u^\sigma\circ\Phi_E)-p\log u\}.
 \tag{23}
\]
原 $r_P$ 的这个 cochain 在相容未分歧整图上是已证明的整对象。
单个 $p$-neighbor 可能需要 ramified 系数域；以下恒等式不额外
宣称每个 neighbor cochain 也整。
在共同特征零系数域的代数闭包中，固定源系数 Frobenius $\sigma$
的一个延拓，并在全部复合式中一致使用它。ramified neighbor 上没有
canonical Witt $\sigma$；这里不宣称该延拓是其模 $p$ Frobenius，
也不由此宣称整性。(24)–(28) 对这个一致所选延拓是纯形式恒等式。

把
\[
 u_G=r^{E/G}_{\varphi_GP}\circ\varphi_G
\]
全拉回同一源曲面。对准确乘积 (7) 应用 (23)，立刻得到
\[
 \boxed{\quad
 \sum_G\mathcal B_{\Phi_E}(u_G)
     =p\,\mathcal B_{\Phi_E}(r_P)
           +\mathcal B_{\Phi_E}(r_{pP}\circ[p]).
 \quad}
 \tag{24}
\]
这是整个二变量正式级数的关系，不只是在模 $p$ 或第一垂直导数成立。

若要把左侧写成商曲面自己的 cochain，
对每个 $E/G$ 另选 $\Phi_G$，则必须保留
\[
 \mathcal B_{\Phi_E}(r'_G\circ\varphi_G)
  =\mathcal B_{\Phi_G}(r'_G)\circ\varphi_G
       +\mathcal E_{G,P},
 \tag{25}
\]
\[
 \boxed{\quad
 \mathcal E_{G,P}
   =\frac1p\log
       \frac{r_G'{}^\sigma\circ\varphi_G^\sigma\circ\Phi_E}
            {r_G'{}^\sigma\circ\Phi_G\circ\varphi_G}.
 \quad}
 \tag{26}
\]
同理，
\[
 \mathcal B_{\Phi_E}(r_{pP}\circ[p])
   =\mathcal B_{\Phi_E}(r_{pP})\circ[p]
       +\mathcal E_{[p],P},
 \tag{27}
\]
其中 $\mathcal E_{[p],P}$ 由 (26) 将 $\varphi_G$ 换为 $[p]$ 给出。
例如取坐标 lift $Z\mapsto Z^p$，
并不能由 $[p]$ 是群同态就断言它与该 lift 交换。
除 $p$ 后的 (26) 正是需要保留的误差，不是可随意删去的规范项。

对未归一 norm，(4) 另给沿基为常数的部分
\[
 \sum_G\mathcal B(\kappa_{\varphi_G,P})
        =\mathcal B(\kappa_{[p],P}),
 \tag{28}
\]
这是 (6) 的完整 cochain 版本。
对常数项采用固定的 $p$-adic logarithm，正式 $t$ 部分取常数为零的
展开，(28) 仍然准确。没有宣称这些各项单独的整性。
将 (24)–(28) 对两个轨道作线性组合时，
应先对各真实单位应用 $\sigma$，再按 (19) 的实际常数取组合；
惰性处 $i^\sigma=-i$ 会产生已知的偶/奇半线交换。

## 8. 为什么固定 κ 的 log 尚未进入中央导数

(4) 中的 $\log\kappa_{\varphi,P}(t)$ 完全不依赖纤维变量 $Z$。
因此对任意 $k\ge1$ 及任意基参数 jet，
\[
 [t^a]\partial_Z^k\log\kappa_{\varphi,P}=0.
 \tag{29}
\]
原来的 $M_e=\partial_Zh_e(t,0)$、
后续实际 GM 临界行及其完整 $p$-adic 中央导数，均从归一后的正垂直
数据构造。(29) 说明一个仅由 (18) 或 (20) 得出的非零单位对数
不会自动进入这些量。

也就是说，本文确实把全部邻点的 norm 常数写成固定单位；
但它在规范化 (21) 时已经被减去。
真正还在 (24)–(27) 中的，是归一 germ、真实同源的坐标/微分因子、
以及 Frobenius–同源换位项。
这些项若能通过实际 Hecke 特征或原 Kronecker 双变量结构进一步控制，
才可能对中央判据提供新信息。

### 已核来源与证明归属

- 实际 $\mathcal S,\mathcal S^{\rm rot}$、$D_N$、$r_P$、
  $d_P$ 的全部好整性：
  [固定除法单位原证明](2026-11-12-weight-one-division-unit-relative-model.md)。
- sigma 的 (1)、同源规范及 (10) 在本文直接推导。
  (4)–(22) 是除子、原点规范和有限核分拆的完整计算，
  没有引用一个未核的 division-resultant 公式。
- Weil reciprocity 的方向另核于 A. Sutherland (2023),
  *18.783 Elliptic Curves, Lecture 23*, Theorem 23.20，p.9，
  [作者正式讲义](https://math.mit.edu/classes/18.783/2023/LectureNotes23.pdf)。
  §2 同时给出本题所需支撑不交版本的直接范数证明。
- 原整 cochain、CM 半线交换和正垂直数据：
  [Kummer Frobenius 原证明](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)。
  (23)–(28) 保留完整形式关系，未把 ramified neighbor 的单项
  误记为已证整的 Frobenius 条目。
