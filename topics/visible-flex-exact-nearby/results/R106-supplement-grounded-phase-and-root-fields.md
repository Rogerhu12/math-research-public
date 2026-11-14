# R106 补充：grounded 首相位与现有真实 root jet 的直接接线

2026-11-12，constructive-route。以下恒等式已经完整证明；新增字段输出还须真实运行。
本补充不更改 R106 原字段、旧 beta 报告或任何几何对象。

## 1. 半核心上的准确消项

R37 已固定真实 $\ell=\partial_\theta\log(F_z/(r|F|))$，
因此 $Y_z=F_z/|F|$ 是同一个实际算子的准确核。
在离腰有正距离的任一半核心上选正高度 $Y=Y_z$ 或 $Y=-Y_z$。
R64 的完整恒等式为
$$
P_g u=Y\widehat P(Yu)=\operatorname{div}(A_g\nabla u),\qquad
A_g=Y^2\widehat A,\qquad d_g=0 .
\tag{106.S1}
$$
不需要 $Y$ 在两半之间保持正；两个半域分别使用自己的正高度，
而包含腰部的中间严格带仍使用原 R106。不能在 $Y_z=0$ 处使用 (106.S1)。

因为 $\mu_g=Y^2\mu$，
$$
\mathcal F_g=\mu_g^{1/2}P_g(\mu_g^{-1/2})
=Y^2\mathcal F,\qquad \mathcal F_g/\mu_g=\mathcal F/\mu.
\tag{106.S2}
$$
这同时证明整个有符号半程首相位没有改变；不只平均不变。
R46 完整 Cauchy 幅度下正 height 的变换也准确抵消，不另加未计的首相位。

记 $L_g=L+2\log Y$。沿用 R106 的原物理缩放系数 $a_0,b_0,\widehat c_0$、
$k=\sqrt{-K_0}$，则实际 grounded 字段是
$$
\boxed{
D_g=-\frac{a_0L_{g,r}^2+2b_0L_{g,r}L_{g,\theta}
                    +\widehat c_0L_{g,\theta}^2}{4k},
\qquad S_g=0,}
$$
$$
V_{g,r}=\frac{a_0L_{g,r}+b_0L_{g,\theta}}k,\qquad
V_{g,\theta}=\frac{b_0L_{g,r}+\widehat c_0L_{g,\theta}}k .
\tag{106.S3}
$$
证明是把 $d_g=0$ 代入 R106 (106.2)，并利用 $A_g/\mu_g=\widehat A/\mu$。
因此
$$
h_\sigma=\frac12\int (D_g\circ\Theta)J\,dr
-\frac14[J(V_{g,r}+\sigma L_{g,\theta})\circ\Theta]_{\rm start}^{\rm end}.
\tag{106.S4}
$$
原先的角散度积分确已消掉，而完整端点仍保留。两个支的主流 $q,\nu$ 不变。

这些量仍只需原六个真实几何二jet及 $K_0,K_0'$。准确地，
$$
(\log Y)_i=\frac{F_{z,i}}{F_z}-\frac{F\cdot F_i}{F\cdot F},
\quad i=r,\theta .
$$
脚本 fourfold_subprincipal_grounded_fields.py 实现 (106.S3)，
单独验证 $F_z$ 非零、$\operatorname{Re}(Y^2)>0$，保留全部复球。
输出中的 $a/\mu,b/\mu,c/\mu$ 是 height 不变比值；
不把原 $a_0$ 错称为新的 $\zeta^2a_g$。

## 2. 根有限部只需 R83 已有的低 jet

在指向负区的真实 $\rho$ 坐标，R83 的 grounded 密度写作
$$
\alpha,\quad \eta,\quad \kappa_{\rm target}=\frac{K_0(r)}{r-t},
\qquad U=\alpha\kappa_{\rm target}\eta,\quad
V_*=\frac{\kappa_{\rm target}\eta}{\alpha},
$$
$$
u=\log U,\quad w=\log V_*,\quad
\mathscr D=-\partial_r+(M/D)\partial_\theta,\quad
s_1=\mathscr Du,\quad h_1=\tfrac12\mathscr Dw-q_\theta.
\tag{106.S5}
$$
R106 的 grounded 根密度因子满足
$$
\kappa_g=\mu_g/\sqrt\rho=\sqrt U,\qquad
\log\kappa_g=u/2,\quad k_*=\sqrt{V_*},\quad Y_0'=1/k_*.
\tag{106.S6}
$$
这来自 $\det A_g=-\rho\alpha\kappa_{\rm target}\eta$。
所以 R106 的所有根减项准确成为
$$
\boxed{
c_0=\frac5{16}Y_0',\qquad c_2=-\frac1{16}Y_0'h_1,}
$$
$$
\boxed{
\widetilde c_{0,g}=-\frac1{16}Y_0',\qquad
\widetilde c_{2,g}=\frac1{16}Y_0'(h_1-2s_1),\qquad
\frac{\sigma}{4}\partial_\theta\log\kappa_g
=\frac{\sigma}{8}u_\theta=-\frac{\sigma}{2}\partial_\theta\log t_0.}
\tag{106.S7}
$$
最后一步用了 R83 的 $t_0=e^{-u/4}$。
所有导数仍是物理根标签；若换为 canonical 或归一标签，须乘真实标签导数。
在 R106 的连续根积分中必须使用同一 grounded height，不能把
$\widetilde c_{2,g}$ 配到原 height 的约化密度。

R99 的冻结 FrameFormula.frame 已在局部实际计算
$DU=s_1,DV,q_\theta$，但旧返回值未保留它们。
新独占 root 适配器复用同一 GridFrame/ComplexFrame 和真实无限 primitive，
另输出 (106.S7)、$s_1,h_1,u_\theta$，不修改旧源与旧报告。
这不需要重新导出 canonical 高阶势，也不把旧缺失字段从浮点摘要猜回。

## 3. 数值身份和真正尚欠的量

新输出必须绑定同一准确 $\delta_5\pm10^{-9}$ 对象、原始 origin/direction、
moving-root 证书、每个真实 common span、无限 primitive 误差和源码 SHA。
在没有真实执行完成前，它们只是可重放的输入接口，没有已完成新报告。

即使根减项已取得，完整角相位仍需根连续余项、严格区真实射线和 $J$、
整个有符号积分及端点。此补充减少实际需要的字段与重复微分，
并未把 R99 的根乘子直接当成 R104 的整个反馈 $b$。

## 4. 精确重放入口

新增源 scripts/fourfold_subprincipal_root_fields.py 的 RootPhaseModel
复用冻结 R99 的 ComplexFrame；只另取该同一局部 jet 中的三个一阶量，
不修改父类的场、根、参数或无限误差定义。它先检查每个真实正因子，
再输出完整根减项。point 与 strip 两种模式的范围分别明示。

从课题根目录执行：

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_subprincipal_root_fields.py --mode point \
 --point 1/16 --out notes/2026-11-12-R106-grounded-root-point.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_subprincipal_root_fields.py --mode strip \
 --strip 1/256 --angle-cells 128 \
 --out notes/2026-11-12-R106-grounded-root-strip.json.gz
~~~

程序默认准确 δ5±1/10^9、Q512、256bit、三次保根区间 Newton。
失败角盒可以有向细分；只有精确有理半 quarter 覆盖检查通过后，
才以已证 D4 奇偶与 Schwarz 共轭扩成全带。奇场的模仍保持。
每个输出保完整输入/源码 SHA 和实际域，两个全相位字段始终为 false。

当前两条新命令尚未执行；之前R106 note的八角运行使用原height字段，
不能转授这里的新根输出。原生/CI可执行资源恢复后须真实重放。
