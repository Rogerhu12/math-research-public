# R105 的实际 Cartesian 图浮点筛选入口

会话：Astra-visible-flex-78718bd0。此记只交付可选轻量诊断工具；
数学恒等式已经完整证明于 R103、R105，不新增完成断言。

## 1. 入口与实际范围

新文件：

    scripts/78718-geometry-arclength-residual-screen.py

调用：

    python scripts/78718-geometry-arclength-residual-screen.py \
      --geometry NEW/prefix-base.json \
      --target NEW/prefix-target.json \
      --out NEW/r105-frozen-target-screen.json

默认取 42 个均匀物理保存坐标点，每个三折周期取 1024 个角节点。
--radial-samples、--angular 可显式改变采样；
--all-nodes 另外加入全部已保存的径向节点，仍不成为连续界。
输出只有每圈的小标量摘要及最坏角节点，不导出图坐标数组。
超过 1 MB 的输出须以 .json.gz 为名，单件仍小于 5 MB。

此工具只接受由目标文件自身绑定的 Cartesian defining base。
如果传入实际 exact-common-cut-prefix，自动安装现有 common-cut
reader，所有圈均评价其**自身修正后的多项式**；修正起点也加入样本，
每行记是否位于修正支持中。不会将 base 的旧值代入该支持。
普通 base 用相同共享节点两 jet、精确保存的 mean increment 重建
长精度 quintic。每 span 只平移平均高度的常数项；所有用于度量的
径向、角向和混合导数保持相同定义，不以 ODE 瞬时 mean velocity
代替保存图的导数。

## 2. 目标度量的限定

目前真实 supplier 的 packet 定义 frozen \(a(s),e(s),e_s(s)\)，
在保存坐标中为

\[
g=ds^2+a(s)^2\,d\Theta^2,\qquad
\Theta=\psi-\frac{e(s)}3\sin(3\psi).
\]

所以本工具明确记录 **frozen target、\(\zeta=1\)**。它不读取旧图的
\(\lambda\)，不把 packet 换名为最终 exact target。当前不存在最终
逐点 \(a_{\rm exact}\) supplier；精确桥报告的
arclength_rescale 在原保存坐标下对应 \(\zeta=1/\lambda\)，
也会改变对应物理半径函数。仅代入 \(\zeta\) 而保留旧 \(a\) 不正确。

未来如果修复后的实际图已经对同一 frozen \(g\) 证明连续误差
\(\varepsilon\)，且**该图自身目标**已有精确桥转移界 \(\eta\)，
既有纯矩阵比较仍给
\(\varepsilon(1+\eta)+\eta\)。这里不复用旧图的 \(\varepsilon\)，
当前浮点筛选也不是该证明。

## 3. 小量计算及不消失的残差

同一实际图的有限 Fourier 系数先组成 \(E,F,G,G_s\)，再在系数层
减去目标，得到 R105 的 \(\Delta_{ss},\Delta_{s\psi},N,N_s,N_\psi\)。
角评价后保留

\[
\rho=1-e\cos3\psi,\quad \nu=-e_s\sin3\psi/3,\quad
b=\nu/\rho,\quad
b_\psi=(\rho_s\rho-\nu\rho_\psi)/\rho^2.
\]

按 R105 计算 \(\varepsilon_{rr},f,\Gamma,h,d\)，尤其 \(h\) 含
\(-bN_\psi\) 和 \(-2\Gamma(a_s/a+b_\psi)\)，没有省去平流项。
这里 \(a_s\) 从同 frozen 参数的实际分段多项式或
\(\sigma\sin\phi\) 公式计算；**不对 packet 的均匀 remainder
界直接求导**。

采用
\[
\ell-1=\left\langle
 \rho\frac{\Gamma}{1+\sqrt{1+\Gamma}}\right\rangle_\psi,\qquad
\ell^2-1=(\ell-1)(2+\ell-1)
\]
避免两个一阶量相减。材料平均按 \(\rho\,d\psi\)。
取样的零均值积分核用三角插值的 Fourier primitive 积分，
锚点为所有圈共同的 \(\Theta(s,0)=0\)。输出移除的数值零频量和
最高三分之一频率的采样 \(\ell^1\) 指标，以显示采样的局限；
二者均不是未截 Fourier 尾界。

每圈输出 \(d\)、\(\ell^2-1\)、\(aJ\)、\(w=f/q-aJ\)，以及

\[
\begin{pmatrix}
\varepsilon_{rr}-2(f/q)aJ+(aJ)^2 & \ell(f/q-aJ)\\
\ell(f/q-aJ) & \ell^2-1
\end{pmatrix}
\]

的采样谱范数，同时保留原图的采样谱范数。两个必要量
\(|d|\)、\(|\ell^2-1|\) 不被这一步重新参数化消去。

## 4. 浮点与连续证书之间的距离

有限残差多项式的角采样数要求大于最高正负频差，因此这些
**有限多项式**本身没有离散别名；开平方、除法及 primitive 的
非线性 Fourier 尾仍未认证。普通 base 的 binary 数据在
longdouble 中重建，报告实际 mantissa 位数；
common reader 的真实有理/区间系数取中点评价，另记其最大系数半径。
target packet 同样取中点并逐圈列出 \(a,e,e_s\) 的已有不确定量。
所有这些误差**没有**通过非线性表达式传播为严格上下界。

因此：

- 输出峰值只在列出的径向点及角节点上成立；
- 采样正性不能证明浸入、全局角向映射或 reach；
- 该工具不构造修复图，不证明 cuff 全二 jet 或固定帽条件；
- 不能把任何采样值作为 README 的 G5 连续度量证书。

## 5. 本次实际执行

尚未对旧候选、warm、低 \(H\) 图或新候选运行此工具；ODE 与
solver 调用数为零。只做三个不读候选的代码级例子：

1. 精确圆柱：修复矩阵采样范数为零。
2. 同圆柱配变化的材料 warp \(e=.1,e_s=.2\)：保留全部平流项后，
   修复矩阵最大浮点值约 \(4.64\times10^{-20}\)；这是坐标项
   消去的实现核对，不是候选证书。
3. 半径 \(1+10^{-5}\) 而目标半径为 1 的圆柱：
   \(d=w=0\)，不消失的周长项保留为
   \(2\times10^{-5}+10^{-10}\)。

真实终端回执 551f85，自然 exit 0。首个真实 inner 到达后仍先执行
raw 入口、实际 base 入口与实际轴点筛选；只有原图的实际瓶颈指向
R103/R105 修复时才运行本可选工具。原图若已通过，不为本接口增加计算。
