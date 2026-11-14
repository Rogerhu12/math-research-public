# 多 ψ 模式的准确负曲率核心与材料控制导数（2026-11-14）

## 用途与界限

新增独立模块 `scripts/warped_ruled_core_controls.py`，不修改已冻结的 `warped_ruled_core.py` 或投影证书。它将两模 ψ 扩展为

\[
 \chi=3\phi,\qquad
 \psi(\phi)=\phi+\sum_{j=1}^M c_j\sin(3j\phi).
\]

可固定强三瓣系数 \(c_1\)，让其他 \(c_j\) 同连接带一起参与后续边值设计；本文件没有运行该优化。核心闭合、单位方向、C3 与半转对称、准确材料度量均保留。模块提供完整端口二 jet 的**固定材料坐标**解析控制导数，以免用固定构造角导数冒充材料导数。

定义中的积分和根为准确数学对象；代码用浮点求积求值，尚不是冻结几何的区间证书。改变球面总长度 \(q\) 会改变度量，必须标为设计；若希望在同一核心度量内调节高模，可另外施加 \(q=q_*\) 这个标量约束。

## 1. 单位方向和只有 c2 参与的闭合条件

记 \(S=\sin\chi,C=\cos\chi,p=\psi'\)，取

\[
 d_{xy}^{\mathbb C}=e^{i\psi}(-S+i\eta C),\qquad
 d_z=-\sigma C,\qquad \sigma=\sqrt{1-\eta^2}.
\]

于是 \(|d|=1\)。以 \(b>0\) 为尺度，定义

\[
 c_\phi=b\,d\times d_\phi.
\]

竖直导数为

\[
 \frac{(c_\phi)_z}{b}=3\eta+p(S^2+\eta^2C^2)
 =3\eta+A p-Bp\cos(6\phi),
\]

其中 \(A=(1+\eta^2)/2\)、\(B=(1-\eta^2)/2\)。由 Fourier 正交性，\(p=1+\sum3j c_j\cos(3j\phi)\) 的均值为 1，且 \(p\cos6\phi\) 的均值只有 \(3c_2\)。因此竖直闭合恰为

\[
 3\eta+A-3Bc_2=0,
\]

或令 \(a=\tfrac12-\tfrac32c_2\)，写为

\[
 a+3\eta+(1-a)\eta^2=0.
\]

选取唯一落在 \((-1,1)\) 的根

\[
 \eta=-\frac{2a}{3+\sqrt{9-4a+4a^2}}.
\]

确实判别式为 \(8+(2a-1)^2>0\)，二次式在 −1、1 的值分别为 −2、4；上述连续根始终落在两者之间。所有 \(j\ne2\) 的高模都不进入这一闭合方程。

对控制的准确导数为

\[
 \eta_{c_2}=\frac{3(1-\eta^2)}{2\sqrt{9-4a+4a^2}},
 \qquad \sigma_{c_2}=-\frac{\eta\eta_{c_2}}\sigma,
\]

其余系数的这两个导数均为零。

### C3 水平闭合与锚点

设 \(T=2\pi/3\)、\(\zeta=e^{2\pi i/3}\)。由于 \(d(\phi+T)=R_Td(\phi)\)，水平导数同样每个扇区旋转一次；三个扇区积分之和为 \((1+\zeta+\zeta^2)I=0\)。令

\[
 I=\int_0^T(c_\phi)_{xy}^{\mathbb C}\,d\phi,\qquad
 c_{xy}^{\mathbb C}(0)=\frac{I}{\zeta-1},\qquad c_z(0)=0.
\]

这确保 \(c(\phi+T)=R_Tc(\phi)\)。半转对称给出 \(I=-\zeta\overline I\)，所以该锚点为实数；实现使用

\[
 c_x(0)=-I_x/2+\sqrt3\,I_y/6.
\]

所有控制导数都包括此锚点的导数，没有逐截面重新置中。

### 显式竖直原函数

将非零频率写成 \((c_\phi)_z/b=\sum_{n\ge1}V_n\cos(3n\phi)\)。先置 \(V_2=-B\)，再对每个 \(j\) 作

\[
 V_j\mathrel{+}=3j A c_j,\qquad
 V_{j+2}\mathrel{-}=\tfrac{3j}{2}B c_j,
\]

以及在 \(j\ne2\) 时

\[
 V_{|j-2|}\mathrel{-}=\tfrac{3j}{2}B c_j.
\]

被省略的零频率已由闭合方程准确消失。故

\[
 c_z(\phi)=b\sum_{n=1}^{M+2}\frac{V_n}{3n}\sin(3n\phi).
\]

模块对这个有限表达式及其控制导数直接求值，不以累计竖直积分漂移定义闭合。

## 2. 正则性、材料角与准确度量

原角方向速度满足

\[
 k^2=|d_\phi|^2=(3+\eta p)^2+\sigma^2p^2\sin^2\chi.
\]

若 \(\sin\chi\ne0\)，也可直接由 \((d_\phi)_z=3\sigma\sin\chi\ne0\) 得正则性。唯一可能退化的位置为 \(\chi\in\pi\mathbb Z\)，因此正则性等价于下列两类因子都不为零：

\[
 3+\eta\Bigl(1+\sum_j3j c_j\Bigr),\qquad
 3+\eta\Bigl(1+\sum_j3j(-1)^j c_j\Bigr).
\]

以正则方向曲线的弧长归一化定义材料角：

\[
 \ell(\phi)=\int_0^\phi k(v)\,dv,\qquad
 q=\frac{\ell(2\pi)}{2\pi},\qquad
 \theta=\ell(\phi)/q.
\]

\(d_\theta\) 的长度恒为 \(q\)，且 \(c_\theta=b\,d\times d_\theta\)。定义

\[
 X(s,\theta)=c(\phi(\theta))+s\,d(\phi(\theta)).
\]

由 \(d\perp d_\theta\)、\(d\times d_\theta\perp d_\theta\)，准确得到

\[
 E=1,\quad F=0,\quad G=q^2(b^2+s^2),\qquad
 K=-\frac{b^2}{(b^2+s^2)^2}<0.
\]

注意 \(K\) 的表达式不含 \(q\)，**并不表示整个周期度量不随 q 改变**。

令 \(P=\phi_\theta=q/k\)、\(Q=\phi_{\theta\theta}=-q^2k_\phi/k^3\)。对于任一原角向量场 \(f\)，材料角二 jet 为

\[
 f,\qquad f_\phi P,\qquad f_{\phi\phi}P^2+f_\phi Q.
\]

分别对 \(c,d\) 使用该公式，就得到 \(X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}\)，其中 \(X_s=d\)、\(X_{ss}=0\)。所需原角导数由

\[
 c_\phi=b\,d\times d_\phi,\quad
 c_{\phi\phi}=b\,d\times d_{\phi\phi},\quad
 c_{\phi\phi\phi}=b(d_\phi\times d_{\phi\phi}+d\times d_{\phi\phi\phi})
\]

直接取得。

半转 \(A_0=\operatorname{diag}(1,-1,-1)\) 满足 \(d(-\phi)=-A_0d(\phi)\)、\(c(-\phi)=A_0c(\phi)\)。速度为偶函数，所以材料角也保持奇性，最终

\[
 X(-s,-\theta)=A_0X(s,\theta).
\]

## 3. 固定材料角的控制导数

下标 \(j\) 先表示固定原角 \(\phi\) 的参数偏导。原角速度导数为

\[
 k_j=\frac{d_\phi\cdot(d_\phi)_j}{k},\qquad
 q_j=\frac1{2\pi}\int_0^{2\pi}k_j\,d\phi.
\]

隐式材料角方程 \(\ell(\phi)=q\theta\) 给出

\[
 \left.\phi_j\right|_\theta
 =\frac{\theta q_j-\int_0^\phi k_j(v)\,dv}{k(\phi)}.
\]

积分与角度在同一展开圈数上计算；周期部分与总长度导数相互抵消。对任一 \(f\)，固定材料角的总控制导数是

\[
 \mathcal D_j f=f_j+f_\phi\phi_j.
\]

因此

\[
 P_j=\frac{q_j}{k}-\frac{q\,\mathcal D_jk}{k^2},
\]

\[
 Q_j=-\frac{2q q_jk_\phi}{k^3}
      -\frac{q^2\mathcal D_jk_\phi}{k^3}
      +\frac{3q^2 k_\phi\mathcal D_jk}{k^4}.
\]

二 jet 的完整参数链式法则为

\[
 \mathcal D_j(f_\phi P)
 =\mathcal D_jf_\phi\,P+f_\phi P_j,
\]

\[
 \mathcal D_j(f_{\phi\phi}P^2+f_\phi Q)
 =\mathcal D_j f_{\phi\phi}P^2+2f_{\phi\phi}P P_j
  +\mathcal D_jf_\phi Q+f_\phi Q_j.
\]

这里 \(\mathcal D_jf_{\phi\phi}\) 含 \(f_{\phi\phi\phi}\phi_j\)，不能省略。代码在此处使用准确三阶原角表达式，并包含闭合根与 C3 锚点的控制偏导。

原角方向导数用复数乘积法求出：若 \(f=-\sin3\phi+i\eta\cos3\phi\)，则水平分量为 \(e^{i\psi}f\)，并使用

\[
 e^{-i\psi}(e^{i\psi})^{(r)}
 =1,\;ip,\;ip'-p^2,\;ip''-3pp'-ip^3\quad(r=0,1,2,3).
\]

这保留所有高频系数及其一次参数导数，没有用数值差分生成 BVP Jacobian。

## 4. 控制空间与稳定 API

```python
core = WarpedRuledCoreControls(coefficients, scale=1, arc_cells=192, quadrature=16)
core.direction_jets(phi)                       # 原角 0..3 阶
core.center_jets(phi)                          # 原角 0..3 阶
core.inlet(theta, s, derivative=0)              # (3, *point_shape, 3)
core.inlet_control_jacobian(theta, s, derivative=0)
                                               # (M, 3, *point_shape, 3)
core.metric(s)                                 # (a, a_s, a_ss)
core.metric_control_jacobian(s)                 # (M, 3, *s_shape)
core.phase_control_jacobian(theta)              # phi_j, P_j, Q_j
core.q_controls                                # dq/d(c1,...,cM)
core.identity()
```

`inlet` 的第一个长度 3 的轴是径向导数 0/1/2，末轴是 Cartesian 分量；`derivative` 是角向导数 0/1/2。控制 Jacobian 最前面增加 \(c_1,\ldots,c_M\) 轴。另提供 scale 的单独端口与度量 Jacobian；它们在固定 \(s,\theta\) 下计算。

后续可固定 \(c_1\)，只取其他列进入优化。若 \(b\) 固定，固定核心度量恰需另外保持 \(q\)；其线性切空间由 \(\sum q_j\Delta c_j=0\) 给出。某个 \(q_j\ne0\) 时可局部用一个高模补偿总长度，仍留下其他控制自由度。这里只给正确约束和导数，不预设所需补偿在整条非线性路径上存在。若 \(b\) 也改变，固定 \(a(0)=qb\) 与 \(a''(0)=q/b\) 同时强迫 \(q,b\) 均固定。

`identity()` 记录全部系数、尺度、锚点规范、总长度积分定义、数值 q 与其梯度、固定环境旋转、求积分辨率及 design 标记。原两模类的函数名和端口轴顺序保持兼容。

## 5. 已执行的廉价检查

`notes/warped-ruled-controls-check-20261114.json` 使用一个人工四模输入，未做优化或几何参数扫描。检查了原角三阶导数、显式竖直原函数、位置与参数积分闭合、准确 E/F/G、完整半转二 jet、两模旧实现兼容，以及固定材料角的 q、phase、端口、metric、scale Jacobian。

完整端口控制 Jacobian 的最大有限差分相对误差约 **2.76e−9**。这些检查验证数值实现与推导一致；准确闭合和等距性来自上述定义与证明，不能由浮点残差替代。Mechanism 代理另已静态复核高模闭合、竖直卷积索引、C3 锚点导数、隐式角导数及端口二 jet 链式法则。

该接口尚未给出嵌入、连续正常弦/reach、圆领封口或可变核心 BVP 的解。下一实际优化须在本公开仓库 Actions 中进行，并明确其目标度量是否随 q 一起设计。
