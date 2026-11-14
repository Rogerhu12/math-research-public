# R6：非平面中央曲线的半转镜合与相位闭族

2026-11-14。独立条件组装证明，扩展 R3。**尚未求得满足全部条件的半带；本结果不是完成标准的实例。** 正面用途是允许准确直纹鞍带作为核心，不再要求中央曲线平面、横向切向恒为竖直方向。

## 1. 精确输入与结论

记 $A=\operatorname{diag}(1,-1,-1)$，即绕 $x$ 轴半转；$Q_\alpha$ 为绕 $z$ 轴旋转。设一个 $C^2$ 正则上半带
$$Y:[0,L]\times(\mathbb R/2\pi\mathbb Z)\longrightarrow\mathbb R^3$$
诱导准确度量
$$g_+=ds^2+a(s)^2d\theta^2,\qquad a>0,\quad a'(0)=0.$$
令中央完整径向二 jet 为
$$\gamma(\theta)=Y(0,\theta),\quad V(\theta)=Y_s(0,\theta),\quad W(\theta)=Y_{ss}(0,\theta).$$
要求以下逐材料角恒等式：
$$\boxed{\gamma(\theta)=A\gamma(-\theta),\quad
V(\theta)=-AV(-\theta),\quad W(\theta)=AW(-\theta).}\tag{1}$$
上半带的末端有一个开平圆领，逐点形如
$$Y(s,\theta)=(r(s)\cos\theta,r(s)\sin\theta,C),\qquad r(s)>0,$$
并以准确位置和二 jet 接到以 $(0,0,C)$ 为中心的平圆盘。圆盘以及该领的材料角均为同一个 $\theta$；不能只匹配边界像。末端半径的方向随图册约定选择，度量满足 $r'^2=1$。

定义中央镜合
$$X(s,\theta)=\begin{cases}
Y(s,\theta),&0\le s\le L,\\
AY(-s,-\theta),&-L\le s\le0.
\end{cases}\tag{2}$$
再以两完整平圆盘封口。假设整个组装确为嵌入：两半带除公共中央圈外无交，圆盘与其余部分除对应接缝外无交，各部分自身亦无交。这是必须实际验证的几何条件，不能由 (1) 推出。

则组装是连通闭 $C^2$ 嵌入球面，度量在带上为
$$g=ds^2+a(|s|)^2d\theta^2.$$
度量和帽上的圆周动作给一个全局材料相位 $\tau_\alpha$。对任意连续 $\alpha:[0,1]\to\mathbb R$，$\alpha(0)=0$，令
$$F_t=Q_{\alpha(t)}\,X\circ\tau_{-\alpha(t)}.\tag{3}$$
这是时间上 $C^2$ 连续的同一度量等距嵌入族，并逐点固定两平圆盘及开圆领中的材料握持区域。其每时刻像为
$$F_t(M)=Q_{\alpha(t)}X(M).\tag{4}$$
所以全时间嵌入性和 reach 都归结为初始整面；含刚体对齐的 $\delta_E=0$。无对齐的 $\delta_{\rm hold}$ 仍需另外给真实像距离见证。

## 2. 中央完整二 jet 的证明

在 $s=0$ 的下侧，由 (2) 得
$$X(0-,\theta)=A\gamma(-\theta),\quad
X_s(0-,\theta)=-AV(-\theta),\quad
X_{ss}(0-,\theta)=AW(-\theta).$$
恰由 (1) 等于上侧。对第一条恒等式作角向一、二阶微分，得到 $X_\theta,X_{\theta\theta}$ 的匹配；对第二条作角微分，得到 $X_{s\theta}$ 的匹配。两片本身 $C^2$，故全部位置二 jet 连续，组装 $C^2$。没有只比较平均中心或法向。

下侧的参数反射同时改变 $s,\theta$ 的符号，$A$ 是环境正交变换，因此拉回度量仍为 $ds^2+a(-s)^2d\theta^2$。$a'(0)=0$ 与中央数据相容。正则性从每侧和匹配的一阶 jet 得到；全局单射性使用明确列出的嵌入假设。

上圆领经下侧变换后为
$$A(r\cos(-\theta),r\sin(-\theta),C)
=(r\cos\theta,r\sin\theta,-C).$$
因而两帽确共用同一个空间 $z$ 轴和同一个材料角，而不是上下两侧相反的相位。开领确保帽接缝的 $C^2$ 匹配。带加两圆盘拓扑上为球面。

## 3. 同一度量、固定握持与全时几何

全局材料圆周动作保持 $g$。空间 $Q_\alpha$ 保持欧氏度量，所以 (3) 对所有时间准确等距。两帽上 $X\circ\tau_{-\alpha}=Q_{-\alpha}X$，故它们在 (3) 中逐点固定；握持集合可取任一闭子盘或两盘的指定子集，但其直径仍须按完整 $D$ 检查。

$\tau_\alpha$ 是全局微分同胚，所以像集恒等式 (4) 成立。环境旋转保持 reach、直径和嵌入性；这一步不要求两半带处于不同的 $z$ 半空间。恰恰因为中央曲线可以非平面，不能再沿用 R3 的“上下半空间自动分离”方便条件，实际全局点对检查不可省略。

对紧材料曲面上的 $C^2$ 图，角平移在 $C^2$ 范数中连续；有限阶导数的一致连续性给该结论。与连续的空间旋转复合即得所需时间连续性。本式不含时间积分或有限时间网格推断。

## 4. 非凸投影也可提供真正像距离见证

设 $K=X(M)$，正交投影 $P(x,y,z)=(x,y)$。若一个紧平面域 $\Omega$ 满足
$$P(K)\subset\Omega,$$
且某个实际点 $p\in K$ 和时刻 $t_*$ 有
$$d=\operatorname{dist}(P(Q_{\alpha(t_*)}p),\Omega)>0,$$
则
$$\boxed{d_H(Q_{\alpha(t_*)}K,K)\ge d.}\tag{5}$$
证明：对所有 $x\in K$，投影不增加距离，故
$$|Q_{\alpha(t_*)}p-x|\ge|P(Q_{\alpha(t_*)}p)-P(x)|\ge d.$$
先对 $x$ 取下确界，再用单侧 Hausdorff 定义即得。它不要求 $\Omega$ 凸，也不把材料点移动距离当作像距离。

因此可检查三瓣星形投影的填充域，而不仅用两个方向的支持差。但**整个过渡和两帽的投影**都必须留在同一个 $\Omega$ 内；仅中央曲线满足这个条件不够。若另已证 $D\le D_+$、$d\ge.3D_+$、全整面 reach$\ge.03D_+$ 及握持直径$\ge.2D_+$，才支付对应完成门槛。

## 5. 一个可直接复用的准确非平面核心

公开旧课题的 `results/R44-explicit-flexible-ruled-saddle-annulus.md` 已给
$$c'_0(\vartheta)=b\,d_0(\vartheta)\times d'_0(\vartheta),\qquad
Z(v,\vartheta)=c_0(\vartheta)+v d_0(\vartheta),$$
其中 $d_0$ 是单位向量，$c_0$ 准确闭合。把全体水平坐标统一旋转 $90^\circ$ 后，其显式 Fourier 式成为
$$c_W=R e^{i\vartheta}+P e^{7i\vartheta}+Q e^{-5i\vartheta},\qquad
c_z=-\frac{b\sigma^2}{12}\sin6\vartheta,$$
$$d_W=i\left(\frac{\eta+1}{2}e^{4i\vartheta}
              +\frac{\eta-1}{2}e^{-2i\vartheta}\right),\qquad
d_z=-\sigma\cos3\vartheta,$$
其中 $R,P,Q,b,\sigma$ 为实数，$\eta=-3+2\sqrt2$。由共轭及奇偶性，准确有
$$c_0(-\vartheta)=Ac_0(\vartheta),\qquad
d_0(-\vartheta)=-Ad_0(\vartheta).\tag{6}$$
球面速度 $|d'_0|$ 是偶函数，因此归一化球面弧长角 $\theta$ 的反函数也是奇函数模周期，(6) 在材料角下仍成立。于是该准确核心的中央数据
$$\gamma=c_0,\quad V=d_0,\quad W=0$$
满足 (1)。若记 $q=\ell/(2\pi)$，其准确度量为
$$dv^2+q^2(b^2+v^2)d\theta^2.$$
这给的是一个真实可用的**入口核心**，不是圆领连接；旧 R44 没有封闭边界，也没有本题所需的宏观比例。R44 原本的四约束可变族不必在此先使用：本结果的相位组装只需要一张满足全部边界条件的静态非旋转半带。

## 6. 非平面 Frenet 核心的另一种入口数据

若另选一条准确闭合、正曲率的单位弧长空间曲线 $\gamma$，以周期材料角表示为 $|\gamma_\theta|=a_0$，取 Frenet 标架 $T,N,B$，可令 $V=B$。则在中央
$$M=-a_0\tau,\qquad Q=a_0^2\kappa,$$
其中 $\tau$ 是挠率。对给定旋转半径的 $a'(0)=0$，Gauss 方程要求
$$W=L N,\qquad L=\frac{\tau^2-a''(0)/a_0}{\kappa}.\tag{7}$$
这是一般非平面输入的具体二 jet 相容式。若 $\gamma(-\theta)=A\gamma(\theta)$，由 Frenet 公式得 $T(-\theta)=-AT(\theta)$、$N(-\theta)=AN(\theta)$、$B(-\theta)=-AB(\theta)$，且 $\kappa,\tau$ 均为偶函数，故 (7) 也满足 (1)。

该观察只在曲率正且标架已定义的范围适用，不能把平面非凸曲线的拐点直接除以 $\kappa$。即使满足入口 Gauss/Codazzi 数据，延拓、圆领、全局嵌入和厚度仍待实际构造。本题继续推进这些条件，未以本条件定理收尾。
