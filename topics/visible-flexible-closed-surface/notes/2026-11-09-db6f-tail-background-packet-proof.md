# 精确背景在物理径向格上的连续 w / wr 包

2026-11-09，`/root/tail_theory`。本稿说明 supplier 的数学包含性；consumer 对显式 Fourier/Hermite 曲面的度量与曲率估计是另一独立模块。当前正式 supplier 脚本 `db6f-tail-background-packet.py` SHA256 为 `75ef3b0426f31926d2e529d18f3b57beda8bc40fdca0cf7f9c26bf33442db1b7`。核心径向 primitive 和稳定 cap 表达式已有未参与者独审；最终 supplier 全文审查及复跑由 root 负责。

## 1. 不变的背景和精确锚点

所有包使用 `2026-11-09-db6f-tail-tight-alpha-proof.md` 的同一精确背景：有限 source 常数是冻结二进有理数，解析函数和径向积分是精确的，全局归一化参数由已审紧区间包围。不同 M、shooting 或径向离散不会改变这些几何参数。

每个 raw profile 的完整径向增量满足

$$\Delta r=A_{n,j}+\alpha B_{n,j}.$$

cell 0 的 A 来自已审高阶积分；内 A 来自已审临界值全变差；cells 0–15 的 B 来自已审高阶积分。从精确 cut 半径出发，以 Fraction 区间倒累加这些增量，即得到每个 profile 左右端点的强包围。此处不使用旧数值径向 primitive 或显示半径当精确锚点。

被审 primitive 模块为 `db6f_tail_background_primitive.py`，SHA256 `9eb20eb44bb202e1dec3df55493ff2ba149b5dc96b340ddf5c5781b46bd65d23`。逐段取

$$f(x)=r_x(x)=A_x(x)+\alpha B_x(x)>0.$$

在一个已确定 cap 分支和绝对值符号的 dyadic leaf 上，用偶数阶 p 的 normalized jet 形成 f 的 Taylor 多项式。将低于 p 的项积分成 P。若 leaf 为 $[m-h,m+h]$，对其中任意 x，积分余项均满足

$$\left|\int_{m-h}^{x}(f-P')ds\right|
\le\sup|f^{(p)}/p!|\frac{2h^{p+1}}{p+1}.$$

这里 p 为偶数，积分核 $(s-m)^p$ 非负；取整 leaf 的绝对余项包围所有 partial primitives。因此端点包围加 $P(x)-P(m-h)$ 和该对称余项包围真实 r(x)。不能确定解析分支的 leaf 使用 $\int_a^x f\in[f([a,b])](x-a)$。每个内部节点同时由左累积和右倒累积包围，再取交；二者都包含同一真值，交集合法。

完整外两层 primitive 为 `2026-11-09-db6f-tail-background-primitive-stable-depth2.json.gz`，包含 18 个 profiles。其稳定 source 模块继承原 Jet/I 类，仅把 cap 导数的同一多项式写成

$$1-35t^4+84t^5-70t^6+20t^7
=(1-t)^4(1+4t+10t^2+20t^3).$$

该函数在 $[0,1]$ 上属于 $[0,1]$，故常数项可与此区间取交，高阶项不作该夹界。此改写及 source `evaluate` 其余部分逐项一致性已由 independent_geometry 独审；不改变背景，只减小自然区间相消。稳定模块 SHA256 `8d485eb6f9cead594ed22ce491d363a3916a418404f905645c7f0eec0bafdcac`。

## 2. 精确物理 span 与近似 inverse

对 int2 表示，每个物理径向节点是保存二进数的精确有理值。对 increment 表示，先精确验证

$$\beta\sum_i\ell_i=r_{outer}-r_{inner},$$

再以 $r_i=r_{inner}+\beta\sum_{k<i}\ell_k$ 定义所有节点。consumer 和 supplier 使用同一个 Fraction 定义，不把显示列当作 increment 模型的节点。

对一个审计子段，以 $\tau\in[0,1]$ 参数化其精确物理半径 $r_{lin}(\tau)$。数值反解仅提供 cubic Bézier 建议 $x_{app}(\tau)$；四个控制数均作为精确二进有理数，并执行

$$0\le a\le b\le c\le d\le1$$

的检查。所以建议 source 坐标始终落在 $[a,d]$，不依赖浮点根求解本身的正确性。

把 $x_{app}$ 代入每个相交 primitive leaf 的多项式，减去精确的 $r_{lin}$，通过 power-to-Bernstein 凸包和 leaf 余项包围

$$|r_{true}(x_{app}(\tau))-r_{lin}(\tau)|\le\delta_r.$$

若一个建议区间穿过多个 leaf，把每个 leaf 的多项式先在整个 $\tau$ 域包围再取最坏值，是对其实际子域包围的放宽，仍然合法。过多微小 leaf 时可直接使用 r 的单调性和两个端点包围；它较粗但不需要逐 leaf 复合。

## 3. w 的多项式包

在一个确定的 cap 解析分支上，把 source 的 w 在 source 中点展开，使用 normalized jet 的 p 阶范围作为 Taylor 余项，再复合 cubic inverse 建议。若分支不确定，直接使用 source w 的区间 range。

由已审整个背景的 $|w_r|<24$，不论真实物理 r 是否恰跨 source profile 接口，均有

$$|w(r_{lin}(\tau))-w(r_{true}(x_{app}(\tau)))|\le24\delta_r.$$

因此把 $24\delta_r$ 加到 source Taylor 余项，即得到真正物理 r 上的包。这只要求两个半径都在完整精确背景的定义域中；supplier 已检有限节点位于 $(r_{cuff},r_{cut}]$。

## 4. wr 的多项式和跨分支回退

wr 需要更紧的局部相位控制。若整个物理子段被强锚严格包含于同一个 source profile，先求一个 forward-certified 反解盒：左端满足 $r(x_L).hi\le r_l$ 或取 source 端点 0，右端满足 $r(x_R).lo\ge r_r$ 或取端点 1。端点退出仅用于属于该 profile 的逆像，不声称覆盖另一个 profile 的点。

将这个真反解盒与 cubic 建议范围取 convex hull J。如果 J 内 cap 分支和 $|w_x|$ 的符号均确定，并且 $r_x\ge m>0$，令

$$q(x)=\frac{w_x(x)}{A_x(x)+\alpha B_x(x)}.$$

用同一 Jet 代数包围 q 的 Taylor 系数、余项和 $\sup_J|q_x|$。严格单调性与中值定理给

$$|x_{true}-x_{app}|\le\frac{\delta_r}{m},\qquad
|q(x_{true})-q(x_{app})|
\le\sup_J|q_x|\frac{\delta_r}{m}.$$

将第二项加到 q 的 source Taylor 余项，就得到真正的 $w_r(r_{lin})$ 包。未确定 cap/abs 分支时不使用高阶导数跨接口，而退回各候选 profile 的直接 $w_x/r_x$ 区间并取 hull；必要时继续审计细分。部分 primitive 表不能仅凭所选 midpoint profile 推断整个物理盒属于内尾。

已审背景证明同时给：在 cell 0 内边界以下，$0\le w\le1/49$、背景曲率不超过 6，因此

$$|w_r|\le6(1+1/49^2)^{3/2}<6.01.$$

supplier 仅在物理盒的右端不超过这一边界的认证下界，或整盒已被某个内 profile 的强锚包含时直接使用该值。整个深圆领也在此范围内。完整内侧粗包已经独审，并由独立 consumer 对圆领及 raw cells 7–2 得到

$$\|g^{-1/2}(X^*e-g)g^{-1/2}\|_{op}
\le4.809212847603965\cdot10^{-7},$$

$$\max|\kappa_i|\le6.169207593957708.$$

这仅是该明确子域的连续结论，不能写成整个曲面的数值。

## 5. degree 8 输出和覆盖

内部 source Taylor 与 cubic inverse 复合后可有 degree 21。最终包只保留 degree 8，对被删除的每个区间系数取 $\max(|lo|,|hi|)$，以向外 I 算术累计；因为 $0\le\tau\le1$，这个和包围被删多项式的绝对值。w 和 wr 分别增加各自余项，接受容差也使用增加后的余项。

每条数据包含 `span_index,u_left,u_right`、w/wr 的上下 power 系数以及两个非负余项。`span_index=-1` 是精确 R6 collar。每个原 span 的子段首端为 0、尾端为 1，邻段二进端点完全相等；consumer 独立检查这一覆盖条件。数据 hash、manifest hash、源/常数表和积分证书 hash 都在 JSON 中绑定。大于 1 MB 的数据自动 gzip，单文件保持小于 5 MB。

粗区与精区交界的某个原 span 可能几乎全部落在 primitive 表更深侧。每个细分子盒都重新检查是否已经落入已证明的粗内域；不能只在父盒检查一次并将下面整段的近似 inverse 永久 clamp 为 0。该工作量问题已修复，旧未完成输出未用于任何 whole-domain 结论。

## 6. 审查范围

此 supplier 只认证同一精确背景的 w/wr 包。完整曲面、接缝、持握见证、非全等、reach 和 README 完成仍需对应独立结论。实际全域 metric/curvature 必须等待完整包生成、consumer 全部行和角向区间运行通过，并把其真实覆盖范围写清楚；小 pilot 的成功不替代这些步骤。
