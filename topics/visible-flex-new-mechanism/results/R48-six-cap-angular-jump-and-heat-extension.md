# R48：六帽反射外延的角跳障碍与保二jet热平滑

日期：2026-11-14。repo_sources 推导，mechanism 独立核，root 全文复核并补充 Gaussian 路径表达。独立完整证明；未运行真实几何评价、扫描或优化。

本稿的否定结论只针对下述**明确有限场类的准确目标积分性**
\(R=V_\theta-\partial_t(aT)=0\)。它不否定准确 S9 六帽，不否定其他连接表示、一般 \(C^2\) 等距连接或给定小容差的近似解；也不直接把 \(R\ne0\) 等同于重构位置的度量必不准确。

准确帽来源是 [六帽构造](R44-S9-six-cap-exact-embedding-and-normal-chord.md)；下面审计的基场形式对应 `scripts/frame_collar_polygonal.py` 的 `reflected_tail_jets` 与 `CompactPolygonalGrid`。代码可继续作为有明确范围的模型，不能把人工微分检查通过当作准确积分性可解。

## 1. 准确帽在顶点的第五角导数

令外半径为 \(R_c>0\)，\(d=R_c\cos(\pi/6)\)，\(w=R_c-d\)。六个法向为 \(n_j=(\cos(j\pi/3),\sin(j\pi/3))\)。各帽采用正幅度 \(A_j>0\) 与

\[
\alpha_j(q)=A_jS_9((n_j\cdot q-d)/w),\qquad
S_9(x)=126x^5+O(x^6)\quad(x\downarrow0),
\]

并在非正自变量上取零。只需 \(0<A_j<\pi/2\)，本稿不依赖幅度相等。沿外圆在相邻两帽间的顶点取 \(\eta=\theta-\theta_v\)，记左、右幅度为 \(A_-,A_+\)。则

\[
\alpha_-(\eta)=L_-(-\eta)^5+O(|\eta|^6)\quad(\eta<0),\qquad
\alpha_+(\eta)=L_+\eta^5+O(|\eta|^6)\quad(\eta>0),
\tag{1}
\]

其中

\[
L_\pm=126A_\pm\left(\frac{R_c\sin(\pi/6)}w\right)^5>0.
\]

用 \(a_n=e_r\cdot n_j\)、\(b_n=e_\theta\cdot n_j\)，准确帽的标量场为

\[
u=\arctan\frac{(1-\cos\alpha)a_nb_n}{1-(1-\cos\alpha)b_n^2},\quad
v=\frac{-\sigma b_n\sin\alpha}{\sqrt{1-b_n^2\sin^2\alpha}},\quad
\beta=-\sigma\pi+\sigma\arctan(a_n\tan\alpha),
\tag{2}
\]

其中 \(\sigma\in\{1,-1\}\) 是上下侧。顶点处左、右 \(a_n=\cos(\pi/6)=c_*>0\)，\(b_n=-b_*\)、\(+b_*\)，\(b_*=\sin(\pi/6)\)。所以

\[
u=O(|\eta|^{10}),\qquad
v=-\sigma b_n\alpha+O(\alpha^3),\qquad
\beta+\sigma\pi=\sigma a_n\alpha+O(\alpha^3).
\]

帽标量场为 \(C^4\)，第五角导数有两侧极限。以右极限减左极限记 \([\partial_\theta^5 f]\)，准确得到

\[
[\partial_\theta^5u]=0,\qquad
[\partial_\theta^5v]=-\sigma b_*5!(L_+-L_-),\qquad
[\partial_\theta^5\beta]=\sigma c_*5!(L_++L_-)\ne0.
\tag{3}
\]

因此相邻幅度不同并不能消去 beta 的跳跃；相邻幅度相等时 v 的该阶跳跃消失，而 beta 的跳跃仍在。

## 2. 被审计的局部反射外延

设连接参数 \(t\) 指向帽，开放准确帽始于 \(t=t_f\)。径向度量函数 \(a(t)\) 满足 \(a(t_f)=R_c\)、\(a'(t_f)=-1\)、\(a''(t_f)=0\)。在左侧短区间令

\[
\varepsilon(t)=a(t)-R_c>0,\qquad
\mathcal E g(t,\theta)=3g(R_c,\theta)-3g(R_c-\varepsilon(t),\theta)
+g(R_c-2\varepsilon(t),\theta).
\tag{4}
\]

所有源半径要求在 \([0,R_c]\)。此处 \(g(r,\theta)=(u,v,\beta)\) 是准确帽的标量场。式 (4) 在 \(t_f\) 保持 value、\(t\)、\(tt\) 以及它们的一个 theta 导数；这是合法的 \(C^2\) 标量外延，**不是**外侧准确帽的等距延伸。

考虑代码中的基场加有限自由列形式

\[
F(t,\theta)=F_{\rm old}(t,\theta;x)
+\chi(t)\{\mathcal Eg(t,\theta)-F_{\rm old}(t,\theta;c_0)\},
\tag{5}
\]

其中 \(c_0\) 固定，\(x\) 为自由系数，\(\chi(t)>0\) 于补丁内部。旧场在 theta 上解析，径向只需在某个内部小区间为 \(C^1\)，其 \(t\) 导数仍在 theta 上 \(C^4\)。固定有限个径向样条结点不会妨碍选取这样的内部小区间。

任取 \(t_0<t_f\) 且 \(\varepsilon(t_0)>0\)、\(\chi(t_0)>0\)。因为两条内圆半径严格小于 \(R_c\)，在顶点附近可取一个**径向与角向的乘积邻域**，使 (4) 的两个内侧取值都在平多边形内，故在那里准确等于 \((0,0,-\sigma\pi)\)。在此邻域 (5) 可以写为

\[
F(t,\theta)=A(t,\theta)+3\chi(t)g(R_c,\theta),
\tag{6}
\]

其中 \(A\) 的 theta 导数解析，\(A_t\) 至少为 \(C^4\)。于是 \(F\) 与 \(F_t\) 都是 theta 的 \(C^4\) 函数；但 (3) 的第五角跳跃保留，乘以 \(3\chi(t)\)。这个乘积邻域是区分 \(C^4\) 角连续性与径向混合导数的关键，不能只在单条径向采样线上作形式判断。

## 3. 任意背景 frame 都不能抵消 beta 的跳跃

写

\[
N=e_r(\theta+u),\qquad
T=\frac{e_\theta(\theta+u)+v e_z}{\sqrt{1+v^2}},\qquad
M=T\times N=\frac{v e_\theta(\theta+u)-e_z}{\sqrt{1+v^2}},
\]

\[
V=\cos\beta\,N+\sin\beta\,M.
\]

对任意有限 \(u,v,\beta\)，准确偏导为

\[
V_v=\frac{\sin\beta}{1+v^2}T,\qquad
V_\beta=-\sin\beta\,N+\cos\beta\,M.
\tag{7}
\]

所以 \(V_v\perp V_\beta\) 且 \(|V_\beta|=1\)。式 (6) 的零至四阶角导数连续，故复合函数第五阶导数两侧之差只含最高阶跳跃：

\[
[\partial_\theta^5V]
=V_u[\partial_\theta^5u]+V_v[\partial_\theta^5v]
+V_\beta[\partial_\theta^5\beta].
\]

结合 (3)、(6)、(7)，得到

\[
\left|[\partial_\theta^5V]\right|
\ge 3\chi(t)\,c_*5!(L_++L_-)>0.
\tag{8}
\]

这个下界是**第五导数跳跃的下界**，不是 \(R\) 的 \(C^0\) 范数下界。

## 4. 准确积分性在此有限类中不可能

由 \(F,F_t\in C^4_\theta\) 以及 frame 公式的光滑性，\(\partial_t(aT)\in C^4_\theta\) 于上述乘积邻域。若准确满足

\[
V_\theta=\partial_t(aT),
\tag{9}
\]

右侧为 \(C^4_\theta\)，便强迫 \(V\in C^5_\theta\)，与 (8) 矛盾。等价地，对两侧的 (9) 求四次角导数，右侧两极限相同，左侧相差 (8) 的非零向量。

因此，只要帽幅度均正、补丁内 \(\varepsilon>0\)、\(\chi>0\)，式 (5) 所定义的**原反射外延加解析自由角列**没有准确 \(R=0\) 解。允许更多同类解析列不能改变这条证明。

本结论不涵盖：

- 更改非解析基场如何随径向传播，或允许适当的非解析自由角列；
- 任意 \(C^2\) 等距连接或准确六帽自身；
- 给定 \(10^{-6}\) 度量误差下的可行性、残差正下界或某个数值下限；
- 只要求重构位置准确等距、却不要求预选 \(V\) 等于其径向导数的其他求解问题。

## 5. 周期热平滑确能移除本稿这条门

令 \(H_\tau=\exp(\tau\partial_\theta^2)\) 为完整周期热半群，作用在**真实连续、已选实 lift**的三个标量场上。令 \(\delta=t_f-t>0\)，选准确规定的 \(\tau(t)>0\)，在端口附近满足

\[
\tau(t)=\kappa\delta^6,\qquad \kappa>0,
\tag{10}
\]

或更一般具有同样正值及一、二阶渐近界的函数。以

\[
\widetilde E(t,\theta)=H_{\tau(t)}\mathcal Eg(t,\theta)
\tag{11}
\]

替换式 (5) 的 \(\mathcal Eg\)，在 \(t=t_f\) 定义为准确端口数据。常数 \(-\sigma\pi\) 被保留；不对 beta 重新取模或逐点选支。

每个固定 \(\delta>0\)，周期热核使 (11) 在 theta 上实解析，故 (8) 所用的固定五阶跳跃消失。这只移除本稿的必要障碍，不证明积分性、非退化、嵌入、幅度或完整 reach。

### 5.1 全部端口二 jet 与 \(tt\theta\) 的连续性

记 \(E=\mathcal Eg\)。准确帽标量场 joint \(C^4\)，因此在有限端口邻域中 \(E\) 及所需混合导数连续且有界。热半群在 theta 上与导数交换，并有

\[
\widetilde E_t=H_\tau E_t+\tau_tH_\tau E_{\theta\theta},
\]

\[
\widetilde E_{tt}=H_\tau E_{tt}
+2\tau_tH_\tau E_{t\theta\theta}
+\tau_{tt}H_\tau E_{\theta\theta}
+\tau_t^2H_\tau E_{\theta^4},
\tag{12}
\]

以及

\[
\widetilde E_{tt\theta}=H_\tau E_{tt\theta}
+2\tau_tH_\tau E_{t\theta^3}
+\tau_{tt}H_\tau E_{\theta^3}
+\tau_t^2H_\tau E_{\theta^5}.
\tag{13}
\]

式 (13) 最后一项不要求未平滑 \(E\) 的第五导数连续。由周期热核的一阶导数 \(L^1\) 估计，存在统一常数 \(C\)，当 \(0<\tau\le\tau_0\) 时

\[
\|H_\tau E_{\theta^5}\|_\infty
=\|\partial_\theta H_\tau E_{\theta^4}\|_\infty
\le C\tau^{-1/2}\|E_{\theta^4}\|_\infty.
\tag{14}
\]

由于 \(\tau_t=O(\delta^5)\)、\(\tau_{tt}=O(\delta^4)\)，(13) 最后一项为 \(O(\delta^7)\)，其他新增项也都趋零。热半群对连续函数的强连续性与 joint \(C^4\) 给其余主项的正确极限。因此 (11) 连续匹配准确帽的

\[
E,\quad E_t,\quad E_{tt},\quad E_\theta,\quad E_{t\theta},\quad E_{tt\theta}.
\tag{15}
\]

并且同样可匹配总阶数不超过二的其他 theta 导数。这里是明确的函数空间与混合导数估计，不能仅由“tau 的前两导数为零”省去 (13) 的潜在奇异项。

### 5.2 支撑、对称与准确身份

仍可在式 (5) 外乘 \(\chi=1-S_9(\delta/h)\)。在补丁另一端，\(\chi\) 的零至四阶所需消失给与旧场的拼接；在帽端 \(\chi(0)=1\)、\(\chi_t(0)=\chi_{tt}(0)=0\)，保留 (15)。要求热时间在每个补丁内部点严格为正，而不是用有限多个零值子段重新引入固定角跳。

周期热半群保留 \(\pi\) 周期、角反射奇偶和实值性，故所选二重六帽的对称约束仍可准确保持。物理模型身份应包含完整帽定义、\(\kappa\) 或完整 \(\tau\) 函数、补丁支撑、固定 \(c_0\)、常数 beta lift、无限周期热半群及原度量身份。改变热时间属于新的基场设计，不是对旧反射连续场的同参数精化。

### 5.3 等价的稳定 Gaussian 路径表达

令 \(Z\) 为标准正态变量，\(\sigma(t)=\sqrt{2\tau(t)}\)，则同一个无限周期热半群也可写成

\[
\widetilde E(t,\theta)=\mathbb E_Z E(t,\theta+\sigma(t)Z),
\tag{16}
\]

其中源函数按 \(2\pi\) 周期理解。在选定 \(\tau=(\delta/h)^6/128\) 时，
\(\sigma=\delta^3/(8h^3)\)、\(\sigma_t=-3\delta^2/(8h^3)\)、
\(\sigma_{tt}=3\delta/(4h^3)\)。直接对路径求导得到

\[
\widetilde E_t=\mathbb E[E_t+\sigma_tZE_\theta],
\]

\[
\widetilde E_{tt}=\mathbb E[E_{tt}+2\sigma_tZE_{t\theta}
+\sigma_{tt}ZE_\theta+\sigma_t^2Z^2E_{\theta\theta}].
\tag{17}
\]

所有被积函数取在 \((t,\theta+\sigma Z)\)。再作一个 theta 导数即可得到 \(tt\theta\)；只涉及总阶数至多三的源导数，没有除以趋零的 \(\tau\) 或 \(\sigma\)。源导数周期、有界，正态变量的各固定阶矩有限，故可由支配收敛直接证明 (15)。这也给 §5.1 的独立核对，且更适合稳定数值评价。

对任意固定有限 Gauss–Hermite 节点，\(\sigma,\sigma_t,\sigma_{tt}\to0\) 也使离散路径的端口 jets 回到准确源 jets（权重归一的浮点误差另记）。但有限平移和仍可能仅为 \(C^4\)，有移动的高阶角跳；它只是 (16) 的求积评价，不能当作已经角解析的连续物理模型。实际计算必须固定无限式 (16)，把求积阶数加倍与位置原函数的角网格加倍分开核对；连续误差认证仍需另付。

## 6. 后续数值实现仍须独立支付的事项

有限 FFT 只能评价上述无限热半群。要把不同角数当作同参数精化，必须锁定同一连续源场和同一 \(\tau\)，不能把每次离散输入的三角插值当作新的物理定义；尤其 \(\tau\to0\) 时不能凭固定截断的平滑曲线宣称端口混合导数已经严格匹配。

实现需要保留 (12)–(13) 的所有链式项、准确端口处的单独分支、实际频谱/求积误差及其加密变化。严格认证还需真实源场连续界、热核截断界与径向积分误差；本稿未计算这些界。固定参数连续场的 \(R\)、实际度量、面积、曲率、全局嵌入和闭面 reach 仍是后续问题。
