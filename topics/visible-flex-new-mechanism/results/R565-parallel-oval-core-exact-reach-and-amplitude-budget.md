# R565：平行椭圆柱核心的准确 reach 与不损失幅度的厚度预算

日期：2026-11-26。会话：Astra-new-mechanism-0105020f-20261126。

**状态：已证明的几何核心及条件组装预算。** 本文给出新的准确 $C^\infty$ 柱面核心，不声称已经构造非圆核心到圆领的完整连接器。它是 O2 的新几何输入，所诱导的核心周长和完整待设计度量与旧固定 $g$ 不同；不能当作旧数值58的同度量精化。

## 1. 构造、材料坐标与完整核心度量

取 $p>q>0,r>0$，令 $K_{p,q}$ 为半轴为 $p,q$ 的实心椭圆，$\overline B$ 为平面闭单位圆盘。以

$$K=K_{p,q}+r\overline B$$

表示它与半径 $r$ 圆盘的 Minkowski 和，$\Gamma=\partial K$。以外法线角 $\phi$ 参数化，置

$$
e(\phi)=(\cos\phi,\sin\phi),\qquad
h_e(\phi)=\sqrt{p^2\cos^2\phi+q^2\sin^2\phi},\qquad h=h_e+r.
$$

它的边界可直接写为

$$
\gamma(\phi)=h e+h'e_\perp
=\left(\frac{p^2\cos\phi}{h_e}+r\cos\phi,
        \frac{q^2\sin\phi}{h_e}+r\sin\phi\right).
\tag{1}
$$

求导得到

$$
\gamma_\phi=\rho(\phi)e_\perp,
\qquad
\rho=h+h''=r+\frac{p^2q^2}{h_e^3}>0.
\tag{2}
$$

故它是正则、严格凸、中心对称的 $C^\infty$ 闭曲线。其两轴支撑分别为

$$A=p+r,\qquad B=q+r,$$

并且全曲线包含在 $x^2+y^2\le A^2$ 和 $|y|\le B$ 中。前一包含关系也可直接由 $K_{p,q}\subset p\overline B$ 得出，不把轴向包围盒误作圆盘。

令

$$a_0=\frac1{2\pi}\int_0^{2\pi}\rho(\phi)\,d\phi,
\qquad \theta(\phi)=a_0^{-1}\int_0^\phi\rho(v)\,dv.$$

则 $\theta$ 是保持方向的圆周光滑微分同胚，$\theta(\phi+2\pi)=\theta(\phi)+2\pi$。用其逆 $\phi(\theta)$ 定义核心

$$X(s,\theta)=(\gamma(\phi(\theta)),s).\tag{3}$$

有 $X_s=e_z$、$|X_\theta|=a_0$、$X_s\cdot X_\theta=0$，所以 (3) **准确**诱导

$$g_{\rm core}=ds^2+a_0^2d\theta^2.$$

任意固定有限 $s$ 区间上，核心光滑嵌入；材料角的内蕴平移仍是等距变换。式 (1)–(3) 给可复现参数化，弧长反函数的数值实现只是对同一个准确定义作求积，不需每网格更换几何。

## 2. 准确 reach，包括非局部点对

定义

$$R=r+\frac{q^2}{p}=\min_\phi\rho(\phi).\tag{4}$$

下面直接证明 $\operatorname{reach}(\Gamma)=R$，不把曲率上界单独冒作完整 reach 下界。

先证明每个边界点有半径 $R$ 的内切圆盘完全包含于 $K$。函数 $h_0=h-R$ 满足 $h_0+h_0''=\rho-R\ge0$，且

$$h_0\ge q-\frac{q^2}{p}>0.$$

令 $c(\phi)=h_0e+h_0'e_\perp$。对固定 $\psi$，

$$\frac d{d\phi}\big(c(\phi)\cdot e(\psi)\big)
=(\rho(\phi)-R)\sin(\psi-\phi).$$

在 $[\psi-\pi,\psi]$ 上导数非负、在 $[\psi,\psi+\pi]$ 上非正。因此 $c(\phi)\cdot e(\psi)\le h_0(\psi)$，而 $\phi=\psi$ 时等号成立。$c(S^1)$ 的凸包 $K_0$ 因而具有支撑函数 $h_0$。支撑函数确定紧凸集，故

$$K=K_0+R\overline B.$$

尤其每个 $P=\gamma(\phi)=c(\phi)+Re(\phi)$ 处，以 $P-Re(\phi)$ 为中心、半径 $R$ 的圆盘包含于 $K$。

任取另一边界点 $Q$，它不在上述圆盘内部。展开平方即得

$$|Q-P|^2\ge -2R,e(\phi)\cdot(Q-P)
=2R\left|e(\phi)\cdot(Q-P)\right|.\tag{5}$$

最后的绝对值来自凸支撑性。这是全部点对的法弦不等式，不是近对角展开。

若距离 $\Gamma$ 小于 $R$ 的平面点 $Z$ 有不同的两个最近点 $P,Q$，光滑最近点条件给 $Z-P=\lambda e(\phi)$，其中 $|\lambda|<R$。等距展开为

$$|Q-P|^2=2\lambda e(\phi)\cdot(Q-P),$$

与 (5) 矛盾。因此 reach 至少为 $R$。

上界可由长轴端的内法线直接看出。设 $P=(A,0)$、$Z_\varepsilon=(A-R-\varepsilon,0)$，$\varepsilon>0$ 足够小。在 $P$ 附近以曲线弧长 $u$ 参数化，有

$$|\gamma(u)-Z_\varepsilon|^2-|P-Z_\varepsilon|^2
=-\frac\varepsilon R,u^2+o(u^2),$$

因为 $P$ 的曲率恰为 $1/R$。所以 $P$ 不是最近点。$A-R=p-q^2/p>0$；$\varepsilon$ 足够小时，另一条轴端 $(-A,0)$ 的距离严格更大，也不可能是最近点。凸性和 (1) 表明 $\Gamma$ 在 $x$ 轴上仅有这两个点，故最近点必离开 $x$ 轴。关于 $x$ 轴反射便给两个不同最近点。最近距离不超过 $R+\varepsilon$，且由 $Z_\varepsilon\to P-Re(0)$ 及已证内切盘性质趋于 $R$。故 reach 不超过 $R$。

对于任意非退化闭区间 $I$，乘积柱面 $C=\Gamma\times I$ 的最近点问题分离成 $\Gamma$ 和 $I$ 两部分，而区间投影处处唯一。因此

$$\boxed{\operatorname{reach}(C)=r+q^2/p.}\tag{6}$$

(6) 包含核心边界，但不把子集的 reach 下界传给尚未构造的完整闭曲面。

## 3. 固定外包络下的严格厚度收益

固定 $A>B>0$，在 $0\le r<B$ 取

$$p=A-r,\qquad q=B-r.$$

所有这些截面保持长短轴支撑 $A,B$、中央见证 $(A,0)$、圆盘半径 $A$ 和条带半宽 $B$。其准确 reach 为

$$R(r)=r+\frac{(B-r)^2}{A-r}
=\frac{B^2+r(A-2B)}{A-r},$$

且

$$\boxed{R'(r)=\frac{(A-B)^2}{(A-r)^2}>0.}\tag{7}$$

这给一条准确光滑核心族，在不扩大支撑预算、不减弱旋转位移见证的条件下增加厚度。$r\uparrow B$ 时 $R(r)\uparrow B$，极限是胶囊形，但本文计算和后续求解均用固定 $q>0$；不以非 $C^2$ 极限或渐近层数冒完成。

本次选定的准确有理参数是

$$p=\frac{17}{20},\qquad q=r=\frac3{20},
\qquad A=1,quad B=\frac3{10},$$

由 (6) 得

$$\boxed{\operatorname{reach}(C)=\frac3{17},
\qquad \max|\kappa_i(C)|=\frac{17}{3}.}\tag{8}$$

同样外轴 $A=1,B=3/10$ 的椭圆柱 reach 为 $9/100$；(8) 是其 $100/51$ 倍。这个比较只针对两个已明确的核心，不宣称完整连接的 reach 已同比增加。

## 4. 对相位闭族的明确条件预算

本核心具有与 R33 相同的开柱端口结构与角平移对称度量；若另构造两侧完整 $C^2$ 等距连接、开放同轴圆领及帽，组装出嵌入 $F_0$，其全局度量对材料角平移不变，则 R33 的

$$F_\alpha=R_\alpha F_0\rho_{-\alpha},\qquad 0\le\alpha\le\pi/2$$

其中 $\rho_\beta$ 表示材料角加 $\beta$。这给固定圆盘握持区的连续等距族，并满足整像 $F_\alpha(M)=R_\alpha F_0(M)$，故如实 $\delta_E=0$。

若完整 $F_0(M)$ 另满足三维球半径 $101/100$、条带 $|y|\le38999/100000$，且完整 reach 至少 $61/1000$，取固定开盘半径 $11/50$，则

$$D\le\frac{101}{50},\qquad
\frac{\delta_{\rm hold}}D\ge\frac{61001}{202000}>\frac3{10},\qquad
\frac{\operatorname{diam}F_0(H)}D\ge\frac{22}{101}>\frac15,$$

以及

$$\frac{\operatorname{reach}(F_0(M))}{D}
\ge\frac{61}{2020}>\frac3{100}.$$

位移见证仍是旋转后的核心点 $(0,1,0)$ 到初始整像的条带距离，不能换成材料点位移。新核心本身满足更紧的 $|y|\le3/10$，且中央宽度取 $w_c=1/50$ 时整个核心在三维球半径 $101/100$ 内；半径 $137/500$ 的圆领投影也位于 $K$，因为 $K$ 包含半径 $B=3/10$ 的圆盘。核心自身 (8) 大于所需 $61/1000$。

**尚未支付的是完整连接器及其度量、跨片点对和支持域。** (8) 不授这些条件；新模型允许在设计阶段寻找新的旋转不变度量，一旦给出候选必须固定该度量和参数后精化。本文没有修改旧固定 $g$、旧58或任何失败运行的判定。
