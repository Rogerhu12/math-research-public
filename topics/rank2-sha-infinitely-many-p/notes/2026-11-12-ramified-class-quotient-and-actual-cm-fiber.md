# 分歧类群的真实 Atkin–Lehner 商与原二阶矩纤维

日期：2026-11-12。**已证明。** 本篇把 R150、R153 的完整
类群和落实为固定商曲线上的实际映射，并在该商上建立原来的
$C_p$ 覆盖、完整 $U$ 迹和算术 Frobenius。原类数不成为一个
额外乘数。尚未证明指定纤维的二阶矩非零。

以下只下降权零函数及到目标椭圆曲线的映射；不把源 Hasse
invariant、Igusa 微分框架自动下降到 Atkin–Lehner 商。
源的简单零仍使用 R153 已付清的平方 Frobenius 比较。

## 1. 固定对象与准确的 Atkin–Lehner 等式

固定 R153 的十六域之一 $F=\mathbb Q(\sqrt D)$。记实际分歧
理想基为 $R_D$，置
$$
 D_0=\prod_{r\in R_D}r,\qquad M=389D_0,\qquad
 X=X_0(M),\qquad h=|\operatorname{Cl}(F)|=2^{|R_D|}.
 \tag{1}
$$
$D_0$ 平方自由。目标、原参数化和完整类群映射是
$$
 E=389\mathrm a1,\qquad \pi:X_0(389)\longrightarrow E,\qquad
 \Phi_D=\sum_{d\mid D_0}\pi d_d,\qquad \Psi_D=[t_0]\Phi_D.
 \tag{2}
$$
$t_0$ 是 R150、R153 统一选定的固定整数。

把开模曲线的点写作
$(A,C_{389},(C_r)_{r\mid D_0})$。$d_d$ 对 $C_d$ 作商并运输
$389$ 子群；$w_r$ 对 $C_r$ 作商，把它换成 $A[r]/C_r$，
同时运输其余循环子群。准确有
$$
 d_d w_r=
 \begin{cases}
 d_{rd},&r\nmid d,\\
 d_{d/r},&r\mid d.
 \end{cases}
 \tag{3}
$$
第二行的两个连续 $r$ 商由
$A/A[r]\simeq A$、即 $[r]$ 给出的同构识别。这个同构保持
$389$ 的循环子群；若记录一个生成元会出现的 diamond 变化，
在这里的 $\Gamma_0(389)$ 模问题上不存在。
所以 (3) 是实际模映射等式，不是忽略尖点常数的 Jacobian
等式。它在紧化上也成立。

不同 $r$ 的商可按任意顺序作，故 $w_r$ 真正两两交换，
$w_r^2=1$。在原最大阶 CM 轨道上它们分别是 R150 的真实
分歧 Artin 类；这些类组成基，因而
$$
 W_R=\langle w_r:r\in R_D\rangle\simeq C_2^{|R_D|},\qquad
 |W_R|=h.
 \tag{4}
$$
由 (3) 直接重排 (2) 的项，得
$\Phi_Dw_r=\Phi_D$、$\Psi_Dw_r=\Psi_D$。

取固定的光滑射影商曲线及商映射
$$
             \rho:X\longrightarrow Y_D=X/W_R.
 \tag{5}
$$
于是存在真正的 $\mathbb Q$-映射
$\widetilde\Phi_D,\widetilde\Psi_D:Y_D\to E$，
使 $\Phi_D=\widetilde\Phi_D\rho$、
$\Psi_D=\widetilde\Psi_D\rho$。

对 R153 的好普通 p，原权零函数准确为
$$
 g_{D,p}=\sum_{d\mid D_0}d_d^*g_p
        =\Theta^{p-2}\bar f_D/\mathrm{Ha}^p,\qquad
 f_D(\tau)=\sum_{d\mid D_0}d f(d\tau).
 \tag{6}
$$
第一式没有额外的 d 权。由 (3)，它也严格 $W_R$ 不变，
故有 $\widetilde g_{D,p}\in\mathbb F_p(Y_D)$，且
$g_{D,p}=\rho^*\widetilde g_{D,p}$。

## 2. 原 CM 中心成为 F 有理点；完整迹不多乘 h

令 $F[c]$ 为导子 c 的环类域，$c$ 素于 $M$。
R150 的分歧 lift 在每个这样的环类群中真为阶二，生成一个
$$
 C_c\simeq\operatorname{Cl}(F)
 \tag{7}
$$
的补群。若 $z_c\in X(F[c])$ 带原 $389$ 理想方向及各分歧核，
则 $w_rz_c=\tau_{r,c}z_c$。这里 $389$ 子群始终同时运输。

在最大阶，$W_R$ 对固定 $389$ 方向的 h 个 CM 点自由传递。
因此
$$
        y_1=\rho(z_1)\in Y_D(F),\qquad
        \widetilde\Psi_D(y_1)=O.
 \tag{8}
$$
另一个 $389$ 方向是其复共轭。$W_R$ 由 CM 线性同源产生，
不交换这两个方向。

现在取在 F 惰性的辅助素数 $\ell$，且
$$
 \ell+1=pu,\qquad p\nmid u.
 \tag{9}
$$
原环类群的准确分解为
$$
 \operatorname{Gal}(F[\ell]/F)=C_\ell\times T_\ell,\qquad
 T_\ell\simeq
 (\mathcal O_F/\ell)^\times/\mathbb F_\ell^\times\simeq C_{\ell+1}.
 \tag{10}
$$
令 $K_\ell=F[\ell]^{C_\ell}$、$y_\ell=\rho(z_\ell)$。
那么 $y_\ell\in Y_D(K_\ell)$，且它在 F 上的稳定子准确是
$C_\ell$：若 $\sigma y_\ell=y_\ell$，商映射的几何纤维使
$\sigma z_\ell=wz_\ell$ 对某 $w\in W_R$ 成立；原带标记
CM 点的 Galois 稳定子平凡，所以 $\sigma\in C_\ell$。
这里原 j 值已在 F 上生成环类域，因而没有遗失更小的稳定子。

令 $U_\ell\subset T_\ell$ 为阶 u 子群，
$L=K_\ell^{U_\ell}$。由 (2)、(7) 得实际整数群等式
$$
 \begin{aligned}
 Q_D
  &=\operatorname{Tr}_{K_\ell/L}
                       \widetilde\Psi_D(y_\ell)\\
  &=[t_0]\sum_{\sigma\in U_\ell}\sum_{\gamma\in C_\ell}
                              \gamma\sigma P[\ell]
   =[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell].
 \end{aligned}
 \tag{11}
$$
因此原来的完整 $C_\ell\times U_\ell$ 迹变成商曲线上真正的
$U_\ell$ 迹。**(11) 没有 h 倍数，也没有除以 h。**
类群和已成为 $\widetilde\Psi_D$ 的一个值。

删去固定有限个坏素数后，各固定 CM 中心仍互不相同。
在这些点 $W_R$ 的稳定子平凡，且 $p\nmid h$，故 $\rho$ 在
这些点 étale。于是 R153 已证明的简单零准确下降为
$$
             \widetilde g_{D,p}(y_1)=0,\qquad
             d\widetilde g_{D,p}(y_1)\ne0.
 \tag{12}
$$
这一步只用商映射在原中心 étale；没有重新认定一个商上的
Hasse invariant 或 $\mathbb F_p$ 椭圆曲线模型。

## 3. 各个分歧 r 在模 ell 下为平方

把 R149 的固定 B 一次增大，使它被
$8\prod_{D\in\mathcal D}D_0$ 及原先所有固定条件整除。
仍在原同一筛法中要求
$$
                           \ell\equiv-1\pmod B.
 \tag{13}
$$
该修改只改变一个固定进程；R149 的绝对系数和 R153 的删除
论证原样适用。

若 $2\in R_D$，则 $\ell\equiv7\bmod8$ 给 $(2/\ell)=1$。
对奇 $r\in R_D$，$\ell\equiv-1\bmod r$ 且
$\ell\equiv3\bmod4$，二次互反律给
$$
 \left(\frac r\ell\right)
 =\left(\frac\ell r\right)(-1)^{(r-1)/2}
 =\left(\frac{-1}r\right)(-1)^{(r-1)/2}=1.
 \tag{14}
$$
故可为每个 r 选择
$\lambda_r\in\mathbb F_\ell^\times$、$\lambda_r^2=r$。

## 4. 真正交换的 full-ell lift 及中心商

先在固定 Weil 配对分量工作。若
$\alpha:\mathbb F_\ell^2\xrightarrow{\sim}A[\ell]$ 是基，
$\phi_r:A\to A/C_r$ 是原同源，定义
$$
      \widetilde w_r(\alpha)=\lambda_r^{-1}\phi_r\alpha.
 \tag{15}
$$
Weil 配对在 $\phi_r$ 下取 r 次幂，在标量 $\lambda_r^{-1}$
下取 $\lambda_r^{-2}$ 次幂。因此 (15) 准确保原配对，
而不是移到一个任意同构的 determinant 分量。

连续两次 r 商的同源为 $[r]$，归一标量为
$\lambda_r^{-2}=r^{-1}$。于是 (15) 的平方在 full ell
标记上也真为恒等。两个不同 r、s 的共同商及标量
$\lambda_r^{-1}\lambda_s^{-1}$ 与顺序无关，故 lifts
两两交换。对任意 $\gamma\in\operatorname{SL}_2(\mathbb F_\ell)$，
$$
 \widetilde w_r(\alpha\gamma)
                   =\widetilde w_r(\alpha)\gamma.
 \tag{16}
$$
因此它们与 full-level 的 $\operatorname{SL}_2$ 作用交换。
改变 $\lambda_r$ 的符号只多出中心 $-I$。

这里要区分两种模问题。在已经带额外 fine level 的基底上，
只改变 ell 标记的 deck 群确为 $\operatorname{SL}_2$；
必须再显式取其中心商。本篇最终的基底是粗曲线 $X_0(M)$，
没有另选一个要保持不动的 fine 标记，故 $\alpha$ 与
$-\alpha$ 由 $[-1]$ 同构。固定配对的中心商
$\mathcal X_\ell\to X$ 的几何 deck 群准确是
$$
                         G=\operatorname{PSL}_2(\mathbb F_\ell).
 \tag{17}
$$
可以先在 fine chart 上作 (15)–(16)，再取中心商并下降到
原 $\Gamma_0(M)$ 模问题；结果相同。

$\ell\nmid M$ 时，$\Gamma_0(M)$ 对模 ell 的约化满射到
$\operatorname{SL}_2(\mathbb F_\ell)$。这也可由模 $M\ell$
的中国剩余定理直接验证。因此上述固定分量几何连通。
素于 p 的 full-level 整模型及其紧化给相同的特征 p
连通覆盖；$p\mid\ell+1$ 不破坏这一点，因为
$p\nmid M\ell$。Cais–Conrad 的 Theorems 2.2–2.3 给出这里
所用的 full-level 好约化与尖点参数。

$W_R$ lifts 与 G 交换，且交平凡：一个同时属于两群的元素
在 X 上恒等，而 $W_R$ 在 X 上忠实。故
$$
 \mathcal Y_\ell=\mathcal X_\ell/W_R\longrightarrow Y_D
 \tag{18}
$$
仍是几何连通的 G-Galois 覆盖。也可直接按函数域次数核对：
$[\mathcal X_\ell:Y_D]=h|G|$，其 $G\times W_R$ 自同构
已有这个阶，取 $W_R$ 不变域恰给 (18)。

## 5. 两个 determinant 分量与真正的 F_p 模型

为了不把所选 $\zeta_\ell$ 误称为 $\mathbb F_p$ 有理，
现在从全部 determinant 分量的 full ell 基出发，除以
所有标量 $\mathbb F_\ell^\times$。所得 projective-level
模问题在基域上定义，几何上有两个分量：Weil 配对的指数
按 $\mathbb F_\ell^\times/(\mathbb F_\ell^\times)^2$ 分类。
其 deck 群为
$\operatorname{PGL}_2(\mathbb F_\ell)$，单个分量的群为 G。

(15) 在 projective level 上就是 $\phi_r$，归一标量消失。
(14) 保证它保持各几何分量。取 $W_R$ 商后，记这个含两个
几何分量、在 $\mathbb F_p$ 定义的 projective 覆盖为
$\mathcal P_\ell\to Y_D$。

固定原 CM 标记给出的 nonsplit 环面及其子群
$$
 T=\mathbb F_{\ell^2}^\times/\mathbb F_\ell^\times,\quad
 |T|=pu,\quad U\subset T,\quad |U|=u.
 \tag{19}
$$
T 的 determinant 平方类映射满射；由于 p 奇，U 的像也
满射。因此 T、U 都交换两个几何分量。准确有
$$
 \begin{gathered}
 T_0=T\cap G,\quad |T_0|=pu/2,\qquad
 U_0=U\cap G,\quad |U_0|=u/2,\\
 Z_T=\mathcal P_\ell/T,\qquad Z_U=\mathcal P_\ell/U,\qquad
 Z_U\longrightarrow Z_T,\quad
 \Gamma=T/U\simeq T_0/U_0\simeq C_p.
 \end{gathered}
 \tag{20}
$$
这些曲线在 $\mathbb F_p$ 定义且几何连通。选任一几何分量
后，它们分别就是 $\mathcal Y_\ell/T_0$、
$\mathcal Y_\ell/U_0$。所以 (20) 没有把 determinant 常数
扩张隐去，也没有改变两个半环面的大小。

此 $C_p$ 覆盖在紧曲线上处处 étale。的确，在原
$\mathcal X_\ell\to X$ 中，开模曲线上的粗模稳定子阶只可能
被 2、3 整除，尖点惯性阶被 ell 整除。取 $W_R$ 商产生的
附加惯性商阶被 h 整除。对 $p\ge7$、$p\nmid h\ell$，
所有这些惯性阶均素于 p；它们与 (20) 的 $C_p$ 群交平凡。
这也给一个不依赖随意 fine 标记的紧化证明。

到固定源商的度数仍为
$$
             \deg(Z_T/Y_D)=\ell(\ell-1),\qquad
             \deg(Z_U/Y_D)=p\ell(\ell-1).
 \tag{21}
$$
本篇移去的是固定的类群因子，并未构造只关于 u 的低次数
覆盖。

## 6. 原 Cartan 标记及算术 Frobenius 没有改变

在特征零先作同一个 projective-level 模问题。
原最大阶 CM 对象的
$\mathcal O_F/\ell$ 作用给一个有方向的 nonsplit Cartan
标记，亦即 T 商上的点。选择这个方向属于原 CM 数据，
不另选其他环面纤维。

对 $\operatorname{Gal}(\bar F/F)$，CM 互反作用运输
$\mathcal O_F$ 自同态及 $389$ 理想核。其最大阶类群分量
准确由某个 $w\in W_R$ 实现。因为分歧同源是 CM 线性的，
该 $w$ 同时运输原 Cartan 标记；在 $W_R$ 商上这个分量被
消去。因此原标记给
$$
                       z_T\in Z_T(F),\qquad z_T\mapsto y_1.
 \tag{22}
$$
这是原 CM 标记的下降证明，不是任意普通点都具有的性质。

在选定的 split p 处，(22) 约化为 $Z_T(\mathbb F_p)$ 的
点。其 (20) 纤维就是原 $\Gamma$-环类商的局部 étale
代数；原生成元和 Frobenius 均保留：
$$
           \operatorname{Frob}_{p,\mathrm{arith}}
                    =s=\operatorname{Art}_p(L/F)=\tau^j.
 \tag{23}
$$
若 $j=0$，纤维为分裂的 $\mathbb F_p^p$ 代数；否则为
$\mathbb F_{p^p}$。在所有矩公式中使用 (23) 匹配后的
$\tau$，不把 $T_0$ 中任意先选的生成元代入。

具体地，原分歧 Artin lifts 的阶都是 2，它们到 $C_p$ 的
像平凡；(15) 的标量在 projective level 已消失。因此这次
下降没有把 s 变成一个未控制的 $C_p$ 平移。原 CM 同源、
类群与 $389$ 子群的运输，也同时证明 (23) 不仅是一个
抽象的同构类型。

## 7. 完整 Hecke 行与原 Q 的无损比较

ell 商与各分歧 r 商的图交换。由 (6) 的 $W_R$ 不变性，
实际分支函数
$$
 h_v=\widetilde g_{D,p}
           (\text{对 }C_v\text{ 作 ell 商后的原层结构})
 \tag{24}
$$
在 $\mathcal P_\ell$ 上有定义；其拉回就是原 $g_{D,p}$ 的
Hecke 行。

T 正则作用于 $\mathbb P^1(\mathbb F_\ell)$。
若 t 生成 T，则完整 U 轨道准确分成
$$
 Uv_0=U_0v_0\ \sqcup\ U_0t^pv_0.
 \tag{25}
$$
定义
$$
 B_\ell=\sum_{v\in Uv_0}h_v\in\mathbb F_p(Z_U).
 \tag{26}
$$
(25) 的两部分都保留，分别有 $u/2$ 项；(26) 的 u 个商上
函数值展开后，恰为原来的 hu 个 level 389 值。
由准确的权零 Hecke 关系及原新形式的 ell 特征值，
$$
 N_\Gamma B_\ell
   =\sum_{v\in\mathbb P^1(\mathbb F_\ell)}h_v
   =a_\ell(E)\widetilde g_{D,p}=:n.
 \tag{27}
$$
R153 的同一输入集合中 $a_\ell(E)\not\equiv0\bmod p$，
所以 n 在原点 (22) 为简单零。这里还用了
$Z_T\to Y_D$ 在这个点 étale：原中心不是椭圆稳定点，
$W_R$ 在其轨道上自由，故 full ell 覆盖在相应邻域是
真正的 étale 群挠子，取 T 商仍 étale。

原 BDP/Buium–Poonen 加法比较在 level 389 的 hu 个真实点
上应用，然后取完整整数和。R134、R139、R153 的微分、
$t_0$ 和基点规范给
$$
 (B_\ell)_{\mathrm{CM}}
       =\epsilon_p\,s(s-\bar a_p(E))\,\bar z_{Q_D},\qquad
 z_{Q_D}=\log_E(Q_D)/p.
 \tag{28}
$$
$\epsilon_p\in\mathbb F_p^\times$ 是同一个已付清的目标
Manin/$t_0$ 规范单位；可同时归一函数使它为 1。
对原 Q 非形式的情形，仍先取 R134 中同一个素于 p 的整数倍
再定义 (28)。没有对各个不整的 $\log/p$ 单独作未经证明的
约化。

由于 $a_p(E)\not\equiv1\bmod p$，
$s(s-\bar a_p(E))$ 在 $\mathbb F_p[\Gamma]$ 中是单位：
其增广为 $1-\bar a_p(E)\ne0$。故对于
$$
 D_1=\sum_{j=0}^{p-1}j\tau^j,\qquad
 D_2=\sum_{j=0}^{p-1}\binom j2\tau^j,
 \tag{29}
$$
原半局部二阶测试与 (26) 的实际纤维二阶矩等价。不存在
一个由于 class quotient 而新增的 h 因子或投影。

最后令
$$
 A=D_1B_\ell,\quad F_2=D_2B_\ell,\quad
 \mathscr D=A^2-nA-2nF_2.
 \tag{30}
$$
R142 的等式 $\tau A=A-n$、$\tau F_2=F_2+n-A$ 使
$\mathscr D$ 下降到底曲线。在原 F 有理点 (22)，由 (12)、
(27) 的简单零，准确有
$$
 D_2(B_\ell)_{\mathrm{CM}}=0\text{ 于整个 }C_p\text{ 纤维}
 \quad\Longleftrightarrow\quad
 \operatorname{ord}_{z_T}\mathscr D\ge2.
 \tag{31}
$$
(31) 如成立仍是原困难；本篇没有证明其不成立。
新结论是：它现在位于一个保原 class trace、原 Cartan
标记和原算术 Frobenius 的真实 $\mathbb F_p$ 纤维上，
而源函数的简单零已由 R153 逐个中心支付。

## 8. 一手来源与本篇新增部分

- B. Conrad（2009），Prasanna 的
  *Arithmetic properties of the Shimura–Shintani–Waldspurger
  correspondence* 附录 A，几何定义及 Lemma A.3。
  [作者全文](https://virtualmath1.stanford.edu/~conrad/papers/prasanna-inv.pdf)，
  作者版印页 60–61；出版版为 Invent. Math. 176 (2009),
  521–600。其实际商公式及 $[Q]$ 识别支持本篇 (3)；
  归一 ell lift (15)–(16) 在本文直接验证。
- B. Cais、B. Conrad，*Modular curves and Ramanujan's continued
  fraction*，2006 年作者版，Theorems 2.2–2.3、式 (2.2)。
  [作者全文](https://virtualmath1.stanford.edu/~conrad/papers/J5final.pdf)，
  印页 4–5。这里用 full-level 模型的好约化、几何连通性、
  Tate 尖点和明确的中心作用；没有用“级别素于 p”偷换
  “覆盖次数素于 p”。
- [R150 完整类群源](2026-11-12-sixteen-fixed-fields-and-complete-class-st-jets.md)
  给实际分歧 lift、完整 Q 及所有中心；
  [R153](2026-11-12-sixteen-unramified-cm-sources-and-square-frobenius.md)
  给新十六域、微分证书、源简单零及同一无穷输入集合。
- [R137 原环面覆盖](2026-11-12-torus-cover-and-actual-cm-trace-row.md)
  给两个半环面轨道与原生成元匹配；
  [R142](2026-11-12-actual-as-basepoints-and-hecke-discriminant.md)
  给 (30)–(31) 的整局部正规形。
  本篇新增的是完整类群的固定 Atkin–Lehner 商、
  determinant 分量的算术下降，以及 (11)、(23)、(28)
  同时保留原对象的比较。
