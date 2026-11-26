# 2026-11-26：自由旋转度量的逆设计与准确开端口

状态：**已证明的表示和误差恒等式；没有成功的新数值候选，未完成课题。**

本笔记服务于会话 Astra-new-mechanism-0105020f-20261126 的新模型，不改变旧真正58的度量、参数或返回结论。搜索阶段允许选择新度量；只有候选定型后的精化才必须固定度量。

## 1. 旋转度量无需先固定径向规范

静态半带 X(s,theta) 的第一形式写成

$$I=E(s,\theta)ds^2+2F(s,\theta)ds\,d\theta+G(s,\theta)d\theta^2.$$

相位组装只要求

$$E=\bar E(s),\qquad F=\bar F(s),\qquad G=\bar G(s),\qquad
\bar E\bar G-\bar F^2>0. \tag{1}$$

不必预先要求 E=1、F=0 或预先给定 a(s)。材料角平移直接保持 (1)。若需要，后处理坐标

$$\vartheta=\theta+\int^s\frac{\bar F}{\bar G}\,du,\qquad
r=\int^s\sqrt{\bar E-\bar F^2/\bar G}\,du$$

将其化为 $dr^2+a(r)^2d\vartheta^2$；这不是设计阶段的额外几何条件。

逆设计可令三个非恒角成分 E−平均E、F−平均F、G−平均G 趋零，同时保均值度量正定和实际面积下界。完整相对误差使用

$$\left\|\bar g^{-1/2}(I-\bar g)\bar g^{-1/2}\right\|_{\rm op}. \tag{2}$$

只有方差变小而面积塌缩，不是一个合格候选。

## 2. 对称性与平均交叉项

一个可选搜索子类为

$$X_x=\sum_{n\ {\rm odd}}a_n(s)\cos n\theta,\quad
X_y=\sum_{n\ {\rm odd}}b_n(s)\sin n\theta,\quad
X_z=z_0(s)+\sum_{n\ge2,\ n\ {\rm even}}c_n(s)\cos n\theta, \tag{3}$$

并允许加入同对称的准确非多项式背景。它满足

$$X(s,-\theta)=\operatorname{diag}(1,-1,1)X(s,\theta),\quad
X(s,\theta+\pi)=\operatorname{diag}(-1,-1,1)X(s,\theta).$$

第一式使 X_s 经过同一正交矩阵、X_theta 多一个负号，所以 E/G 偶、F 奇；第二式使三者均为 pi 周期。故 E/G 只有 cos(2k theta)，F 只有 sin(2k theta)，平均F准确为零。非零 c_n 允许真实非平面角截面，未落入 R63 的水平角切向类。

解除此对称时，可保留非零平均F，并允许圆领材料相位 phi_cap 自由；r(s)e^{i(theta+phi_cap)} 仍精确等变。试验子类失败不排一般几何。

## 3. 开核心和开圆领如何准确固定

固定 $0<s_{\rm in}<s_{\rm out}<1$，令 $u=(s-s_{\rm in})/(s_{\rm out}-s_{\rm in})$。用

$$\eta(u)=0\ (u\le0),\quad \eta(u)=e^{-1/u}\ (u>0),\qquad
\chi(u)=\frac{\eta(u)}{\eta(u)+\eta(1-u)}. \tag{4}$$

在 u<=0 置chi=0，在 u>=1 置chi=1，所有非零阶端导数为零。设 gamma(theta) 是准确弧长角核心，|gamma_theta|=a0，并取固定 w,L_c,r_c,L_r,z_cap。令

$$C(s,\theta)=(\gamma(\theta),w+L_cs),$$
$$P(s,\theta)=((r_c+L_r(1-s))\cos\theta,
(r_c+L_r(1-s))\sin\theta,z_{\rm cap}),$$
$$X_{\rm bg}=(1-\chi)C+\chi P.$$

自由表示可写

$$X=X_{\rm bg}+\beta(u)\sum_jB_j(u)V_j(\theta),\qquad
\beta(u)=
\begin{cases}e^{4-1/u-1/(1-u)},&0<u<1,\\0,&\text{otherwise}.
\end{cases} \tag{5}$$

多项式 B_j 给 C-infinity 表示；三次简单结点 B 样条给 C2，五次给 C4。乘 beta 不会改善内部结点的正则性。

对所有自由系数，整个 s<=s_in 前缀准确为开柱，整个 s>=s_out 后缀准确为开平圆领。不是仅匹配边界两个二 jet，也不是将指数小尾误认为零。实现必须在这些区间直接赋精确零/一。

末领接平盘 r<=r_c，中心用 Cartesian 图；中央开柱与镜射负侧也有完整开邻域相容。此表示不自动保证无自交。

**后续结构提醒：** C-infinity 阶跃本身不产生无限次曲率变号。第7节的原始文献核查说明，若希望沿径向图的非径向全平分支求解，还需要振荡尾；可见[R566的固定振荡尾](../results/R566-flat-oscillatory-cap-tail-and-graph-reach.md)。

## 4. 平行椭圆的准确材料角

支撑函数

$$h(\varphi)=r+\sqrt{p^2\cos^2\varphi+q^2\sin^2\varphi},\qquad p\ge q>0$$

给核心

$$\gamma(\varphi)=
\left(\frac{p^2\cos\varphi}{f},\frac{q^2\sin\varphi}{f}\right)
+r(\cos\varphi,\sin\varphi),\qquad f=\sqrt{p^2\cos^2\varphi+q^2\sin^2\varphi},$$

$$\rho=r+\frac{p^2q^2}{f^3},\quad
a_0=\frac1{2\pi}\int_0^{2\pi}\rho,\quad
\theta(\varphi)=a_0^{-1}\int_0^\varphi\rho. \tag{6}$$

于是 $\gamma_\theta=a_0(-\sin\varphi,\cos\varphi)$。弧长反函数的数值精化须始终逼近同一个 (6)，不能换核心几何冒称同一精化。按弧长的非圆平面核心一般不是有限傅里叶多项式。

## 5. 局部非平面初值与解析Jacobian

R2 已给正曲率核心的局部 Cauchy 入口，此处只写可用于新初始化的 jets。向外法向 n、曲率半径 rho，若 a(0)=a0、a'(0)=0、a''(0)=a2、a'''(0)=a3 且 X_s(0)=e_z，则

$$X_{ss}(0)=\frac{a_2\rho}{a_0}n,\qquad
X_{sss}(0)=\frac{a_3\rho}{a_0}n-\frac{a_2^2\rho^2}{a_0^2}e_z. \tag{7}$$

这是 Gauss/Codazzi 和单位径向速度的直接结果。第三阶高度有真实角依赖，不能只插值平截面。截断 Taylor 式不是准确解；第四阶位置还影响第三阶交叉度量。若强制完整开柱，不能在同一点又指定非零 a2。

位置的一阶变化给

$$\delta E=2X_s\cdot\delta X_s,\quad
\delta F=\delta X_s\cdot X_\theta+X_s\cdot\delta X_\theta,\quad
\delta G=2X_\theta\cdot\delta X_\theta. \tag{8}$$

对称类中用 e=E/Ebar−1、g=G/Gbar−1、f=F/sqrt(Ebar Gbar)，

$$\delta e=\frac{\delta E}{\bar E}-\frac{E\,\delta\bar E}{\bar E^2},$$
$$\delta f=\frac{\delta F}{\sqrt{\bar E\bar G}}
-\frac f2\left(\frac{\delta\bar E}{\bar E}+\frac{\delta\bar G}{\bar G}\right).$$

逆设计阶段均值的变化必须计入Jacobian，冻结度量精化阶段才不计。

## 6. 全角覆盖、固定度量和全相位

若整个 X 在角变量的度数确实至多N，则 E/F/G 度数至多2N，至少4N+1个等距节点可在准确算术下无混叠重建。准确非多项式核心背景不满足这个假设；这时须控制背景傅里叶尾/导数，或做连续区间包围。不能误用有限Nyquist结论。

搜索每一步重新计算均值度量叫逆设计。候选定型后必须固定一个径向函数 g_* 的完整定义，后续只优化位置并令 I−g_* 下降；每步继续改均值不是固定g精化。

对固定旋转度量 g_*，$F_\alpha=R_\alpha X(s,\theta-\alpha)$ 的度量误差张量仅被材料等距拉回，最大相对误差与alpha无关；初态的嵌入与reach经刚转传到全相位。所有初态连续空间门及宏观幅度仍需实际支付。

## 7. 原始文献对数值入口的限制

已直接读 Boyang Hu, *Smooth isometric bending of a closed sphere*, 2026, https://hexagonmath.org/2611.00534v1 的 §3.2、§4.2、§4.4–4.6、§5.1–5.9、§10.3–10.5、附录A。

Proposition 3.2 在径向图度量的径向高度处给线性角模
$$(wf')'-j^2w'f/r=0.$$
若正实斜率w在flat端单调，f与通量wf'同时趋零就只能f=0。它不等于所有远离径向图的非线性构造都被排除，但说明仅C-infinity截断没有买到原论文的seed。

论文Morse cell用 $\rho_n=A_n(e^{-X}-e^{-2X})-B_n$、$r_{XX}=-\rho_nr$、$w=\lambda_n r_X$；$d_n\asymp e^{n^2}$，
$$A_n=(d_n^{-1/2}+2d_n^{-9/2})^2,\quad B_n=d_n^{-9},\quad
\lambda_n=e^{-n^{5/2}}\prod_{k=N}^n\sigma_k,\quad 1\le\sigma_k\le2.$$
cell长约e^{-n²}、连接约A_n^{12}、seed衰减约e^{-2n³/3}。sigma序列还用全频带测度排除及对角极限选择；文中未交付机器数列，N和buffer常数也未量化。因此不能把任意有限cell拼接称为论文的完整输入。

Theorem10.3的 $z_q=h_{w_q}+qu_q$ 同时改变 $w_q$，其改变量O(q²)；q只选择一张面/一份度量，固定q后的相位才是固定g弯曲。没有可直接给本题.3D/.03D的数值参数。整体相似缩放保持这些比例；小q端的非径向偏离和相位像变化均为O(q)。

附录A证明：准确Darboux高度的平方若角向有限Fourier且在一个开领径向，则处处径向。因此固定有限角阶直接高度只能作加密近似，不能当准确非径向终点；非线性单位切向T表示一般有无限角谱，不自动受此有限类排除。

当前没有新的完整闭面，本文不将这些表示或条件当成完成。

