# R719　固定前三个 Fejér 模式时任意当前高模仍保留的轴差

2026-11-27，geometry，AI 辅助。**状态：完整条件性解析证明；没有科学运行，没有实际候选的全角正性、全像距离或比例结论。**

[R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 给出固定的准确 dyadic Fejér 参考图，且明确其余 157 个当前核心系数仍自由。本文不继承初点七模的轴值，而是在**全部当前曲率半径准确严格为正**的条件下，统一控制所有自由高模可能造成的抵消。结论对任意有限 \(M\ge3\) 成立，因此也保留 current M320 的全部模式。

定向核读 R1 的固定二模核心、R717 全文及 R718 的整像流下界后，未见下面的固定前三模式、任意高模结论。R1 的具体轴差不被迁给当前场；R718 的全闭面条件也未被本文替代。

## 1. 对象与命题

设
\[
p(\theta)=1+\sum_{j=1}^{M}c_j\cos(2j\theta),\qquad
\rho(\theta)=p(\theta)+p''(\theta)
=1+\sum_{j=1}^{M}(1-4j^2)c_j\cos(2j\theta).
\tag{1}
\]
要求
\[
\rho(\theta)>0\qquad\hbox{对全部 }\theta\in\mathbb R. \tag{2}
\]
这不是有限角网的 sampled positivity。原 source 的有限域检查未单独支付 (2)。

前三系数固定为 R717 预先定义的最近偶数 binary64 值，按准确二进有理数解释：
\[
c_1={7\over16},\quad
c_2={\rm RN}_{64}(-3/40),\quad
c_3={\rm RN}_{64}(3/112).
\tag{3}
\]
其余 \(c_4,\ldots,c_M\) 全部任意自由，只须共同满足 (2)。记
\[
\epsilon=2^{-53},\qquad
c_2=-3/40+\delta_2,\quad c_3=3/112+\delta_3,\quad
|\delta_2|,|\delta_3|\le\epsilon. \tag{4}
\]
\(c_1=7/16\) 准确可表示，没有给它虚加舍入误差。

核心支撑曲线是
\[
\Gamma(\theta)=p(\theta)e_r(\theta)+p'(\theta)e_t(\theta).
\]
其四轴坐标为 \((\pm X,0),(0,\pm Y)\)，其中
\[
X=1+\sum_{j=1}^{M}c_j,\qquad
Y=1+\sum_{j=1}^{M}(-1)^jc_j. \tag{5}
\]

**命题。** 在 (1)–(4) 下，
\[
X>0,\qquad Y>0,\qquad
\boxed{\,X-{7\over3}Y>{1\over2520}-{14\over3}\epsilon>0\,}, \tag{6}
\]
并且
\[
\boxed{\,X-Y>{169\over210}-2\epsilon>{4\over5}\,}. \tag{7}
\]
特别地，完整当前核心始终有
\[
\boxed{\quad X/Y>7/3.\quad} \tag{8}
\]
这里没有限制自由高模的符号、没有把它们设零，也没有令 current M 回退到 reference M。

## 2. 正密度给全部 Fourier 系数的统一界

由 (1)，\(\rho\) 为 \(\pi\)-周期且
\[
\int_0^\pi\rho(\theta)\,d\theta=\pi.
\]
对每个 \(j\ge1\)，Fourier 正交性给
\[
(1-4j^2)c_j={2\over\pi}
\int_0^\pi\rho(\theta)\cos(2j\theta)\,d\theta.
\]
用 \(\rho\ge0\) 和 \(|\cos|\le1\)，得到
\[
|(1-4j^2)c_j|\le2,\qquad
\boxed{\ |c_j|\le{2\over4j^2-1}.\ } \tag{9}
\]
有限 \(M\) 之外可仅在数学估计中记 \(c_j=0\)，不会改变原场或变量数。即使 \(M\) 改变，正的上界尾和仍可用同一无穷和控制。

式 (9) 是非负密度的必要后果，不能反过来用逐系数界宣称 (2) 成立，也不把 \(\sum(4j^2-1)|c_j|<1\) 这种过强充分条件施加于当前 Fejér 族。

## 3. 两个高模尾和的准确值

恒等式
\[
{2\over4j^2-1}={1\over2j-1}-{1\over2j+1} \tag{10}
\]
把奇、偶自由模式分开。令
\[
O=\sum_{\substack{j\ge5\\j\ {\rm odd}}}{2\over4j^2-1},
\qquad
E=\sum_{\substack{j\ge4\\j\ {\rm even}}}{2\over4j^2-1}.
\]
每一项均为正，级数绝对收敛。于是
\[
O={1\over9}-{1\over11}+{1\over13}-{1\over15}+\cdots
={\pi\over4}-{76\over105}, \tag{11}
\]
\[
E={1\over7}-{1\over9}+{1\over11}-{1\over13}+\cdots
={13\over15}-{\pi\over4}. \tag{12}
\]
这里使用
\[
{\pi\over4}=1-\frac13+\frac15-\frac17+\cdots.
\]
这个准确恒等式由把 \(1/(1+x^2)\) 的有限几何展开在 \([0,1]\) 积分、再令余项趋零得到；余项的积分绝对值不超过 \(1/(2n+3)\)。没有用浮点 \(\pi\) 或截断有限项猜测级数值。

结合 (9)，对任意有限当前 \(M\) 有
\[
\left|\sum_{\substack{5\le j\le M\\j\ {\rm odd}}}c_j\right|\le O,
\qquad
\left|\sum_{\substack{4\le j\le M\\j\ {\rm even}}}c_j\right|\le E.
\tag{13}
\]
也有 \(O+E=1/7\)，与 (10) 的完整尾和一致。这里的无穷和只是一个上界证明，没有把无穷个变量加入求解。

## 4. 保留任意高模后的轴比

由 (5)，
\[
X-\frac73Y
=-\frac43+\frac{10}3
\sum_{\substack{1\le j\le M\\j\ {\rm odd}}}c_j
-\frac43\sum_{\substack{1\le j\le M\\j\ {\rm even}}}c_j.
\tag{14}
\]
前三个理想有理值的贡献准确为
\[
-\frac43+\frac{10}3
\left(\frac7{16}+\frac3{112}\right)
-\frac43\left(-\frac3{40}\right)=\frac{11}{35}. \tag{15}
\]
由 (4)，舍入修正是 \(10\delta_3/3-4\delta_2/3\)，其下界为 \(-14\epsilon/3\)。再用全部奇、偶自由尾的 (13)，
\[
\begin{aligned}
X-\frac73Y
&\ge \frac{11}{35}
-\frac{10}{3}O-\frac43E-\frac{14}{3}\epsilon\\
&=\frac{11}{7}-\frac{\pi}{2}-\frac{14}{3}\epsilon.
\end{aligned} \tag{16}
\]
到这一步，所有有限当前高模都已包括，不需要知道它们的具体输出字。

为得到 (6) 的明确有理余量，消费 [R712](R712-full-positive-radius-central-second-derivative-comparison.md) 式 (12) 已证的恒等式
\[
\frac{22}{7}-\pi
=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx. \tag{17}
\]
在 \(0<x<1\) 上 \(1/(1+x^2)>1/2\)，而有限多项式积分给
\[
\int_0^1x^4(1-x)^4\,dx
=\frac15-\frac46+\frac67-\frac48+\frac19
=\frac1{630}.
\]
因此
\[
\frac{22}{7}-\pi>\frac1{1260},
\qquad
\frac{11}{7}-\frac{\pi}{2}>\frac1{2520}. \tag{18}
\]
(16)–(18) 给 (6)。最后一个量严格为正，例如
\[
14\cdot2520<3\cdot2^{53}
\]
就是相应准确整数不等式。这里明确使用了 (17) 的积分下界加强量；单独一句 \(\pi<22/7\) 不足以给 \(1/2520\) 的数值余量。

## 5. 两半轴为正以及统一核心差

正性直接来自 \(\pi\)-周期 \(p\) 的准确恒等式
\[
2p(\theta)=\int_0^\pi\rho(\theta+t)\sin t\,dt. \tag{19}
\]
证明是把 \(p+p''\) 分部积分两次：内部两项相消，边界留下 \(p(\theta+\pi)+p(\theta)=2p(\theta)\)；含 \(p'\) 的端点项因 \(\sin0=\sin\pi=0\) 消失。由 (2) 和 \(0<t<\pi\) 上 \(\sin t>0\)，得到所有 \(\theta\) 的 \(p(\theta)>0\)，特别 \(X=p(0)>0\)、\(Y=p(\pi/2)>0\)。这不需要另外重做凸性证明。

等价地，轴上可写
\[
X=\frac12\int_0^\pi\rho(t)\sin t\,dt,\qquad
Y=\frac12\int_0^\pi\rho(t)|\cos t|\,dt.
\]
现在可由 (6) 除以已经证明的 \(Y>0\)，得到 (8)。

轴差只含奇模式：
\[
X-Y=2\sum_{\substack{1\le j\le M\\j\ {\rm odd}}}c_j
\ge2\left(\frac{13}{28}-\epsilon-O\right)
=\frac{499}{210}-\frac{\pi}{2}-2\epsilon. \tag{20}
\]
由 R712 的 \(\pi<22/7\)，
\[
X-Y>\frac{169}{210}-2\epsilon>\frac45,
\]
因为 \(169/210-4/5=1/210>2^{-52}\)。这完成全部命题。

## 6. 接入 R718 时可以消去哪一项实际数值依赖

若某个实际完整当前点满足本文条件，且已经按 [R718](R718-positive-definite-flow-distance-and-whole-image-held-witness.md) 支付同一中心 \(0\)、同一个 \(A_\beta=\operatorname{diag}(1,1,\beta)\)、完整闭面共同支撑 \(\sigma>0\)、准确 core \(z=0\) 端口和 quarter-phase 成员关系，则本文给一个统一的
\[
r_-=7/3.
\]
因此记 \(m=\min(1,\beta)\)，有
\[
\boxed{\quad
\delta_{\rm hold}\ge
\frac{\sigma}{m}\left[\left(\frac73\right)^m-1\right].
\quad} \tag{21}
\]
这里所有帽、标记、上下片都仍由 R718 的**完整目标支撑**控制；本文的 (7) 绝不是完整目标距离。

若 \(m=a/b\) 为正有理数，R718 的证据接口现在可选择任意准确有理 \(\Lambda\ge1\) 满足
\[
\Lambda^b\le(7/3)^a,
\]
然后得到准确有理下界 \(\sigma(\Lambda-1)/m\)。或将所需 \(D_+/5\) 直接代入 R718 的整数幂充分判据。这不生成新的 \(F\)、normal root 或六 jet。

当前实际 \(X/Y\) 可能比 \(7/3\) 大；若完整当前系数已读取并验证，可使用更强的实际比值。本文没有禁止既有完整点读取，也不允许省去实际 source/model/point/snapshot 身份：它只在**数学估计**中统一控制自由高模，而非把实际点当作初点。

## 7. 与已有结果和实际入口的边界

R717 的参考七模正性、初始轴值和初始曲率界仍只属于其明确的参考图；本文没有把那些数值迁给任意当前核心。这里的新当前结论来自固定前三值加整个当前 \(\rho>0\)，逐一包括剩余全部自由模式。

M160、M320 或 N4096/current observer 的真实源码仍须证明它们固定的是 (3) 的同一准确字、保持 (1) 的完整当前模式含义。参考 M160 的系数数组不能替代 current M320 数组；不同 point 不可混用。当前 normal 成功、有限 16384 角 domain 检查或可变 progress 都不单独证明 (2)。

(6)–(8) 仅是核心的统一形状事实。整张闭面可能有比核心更接近旋转见证的其他点；只有 R718 的完整共同支撑或 R717 的全目标盒排除才能进一步给整像距离。完整 \(D\)、\(\delta_{\rm hold}\ge D/5\)、reach≥\(3D/100\)、同场 metric \(10^{-6}\)、固定握持区大小和 \(\delta_E>0\) 都未在本稿中被宣布完成。

原全部变量、三路 SO3 通道、径向域、角域、32 normal stages、科学预算和实际精化入口保持。没有数值 fixture、额外 scan 或新的求解准入门。
