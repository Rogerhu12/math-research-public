# 真实低曲率尾的实际参数与端口（工作中）

会话：Astra-visible-flex-4ffd372b / closing_geometry。2026-11-09。数值可行性，不是闭曲面或精确非线性尾定理。

## 已找到的实际尾

保留已存在 `f6tail_compact_controlled_tail.mjs` 的 **真实积分定义背景**（并非 synthetic scaled_port），参数见 `closing_tail_r06_k5_candidate.json`：
rCut=0.6, wCut=0.01, width=0.35, rCuff=0.25, curvatureBound=5,
delta0=.006, R=64, a=2.75, etaPower=1.5, etaRatioAtN0=.05,
orientation=+1, prefixR=2, prefixEnd=15, prefixReturnStart=8, protectCell=80,
slopeCap=.1, capTransition=2, calibrationSteps=1024, warpSteps=16, quadratureTolerance=2e-11, cuspAwareQuadrature=true.

积分重分配 alpha=61.80789156392591>0；最小所需径宽0.1774292154701811<0.35；
经线长度0.35056452239677094，高度增量0.015088340437122386；
两个端口的r/w/w_r接缝误差均约1e-16；deepSource保留未改。
背景 meridian |kappa|≤5 的公式性预算成立于chi=1区域，chi混合buffer采样最大0.277；
因此尚须严谨包络buffer+deep，但旧95并非新的必然代价。
angular curvature粗界 .1/.25=.4，因此此背景不存在95级曲率障碍。

给数值同伴的 **实际物理线性DN**：`closing_tail_r06_k5_port_m12.json`，角频2,4,...,24。
m2 cutoff u_r/u = -5.313476177227717。
步数256→512该m2变化1.99e-7、方向变化1.82e-8；far40→64在本次浮点完全相同。
全M12最坏方向加密变化7.34e-8。此文件并非无限尾或非线性DN认证，需后续加密/接实际非线性解。

rCut=.6,wCut=.01 的原 DirectionalBridge 从r=1接入所需L=0.65943046358317；
采样桥最大曲率3.579724904631988，高度0.3986100470665984。
所以保留r=.6比r=.8更适合预算：.8新桥曲率7.099而.6仅3.58。
完整桥扫描 `closing_bridge_scan.json`。

## 剩余硬问题

1. 此真实DN改变prefix边界问题；必须重求delta并检查非线性，不可直接拼现有synthetic解。
2. wCut=.01相当平，原prefix截面非圆高度约.005需由真实非线性方程检验。
   **勘误：早期把 |u_theta|<r*w 称作图型必要约束不正确，撤回其纯m2幅度.003障碍。**
   实际角投影条件为 |u_theta|<r；r*w界只给归一化量P=u_theta/(r*w)的小量充分假设。
   非线性root还有D/A条件，不能由这条勘误反推给定幅度已经可行。
3. 正在扫描改变有限原始cell尺度/指数以支持wCut=.1–.5，同时保留kappa≈5；
   新a不可直接套原R20/R520精确尾结论。
4. 整闭reach仍须prefix-tail混合点对；局部κ达标并不意味着reach达标。

## 实现与来源核验

`scripts/closing_tail_scan.mjs`、`closing_tail_port.mjs`；
依赖9个本机旧cache源码的Git blob已逐个与连接器当前main核验一致，
具体表 `closing_tail_dependency_blobs.json`。
尚未把低曲率tail宣传为完整可行构造。


## 2026-11-09 后续：较大cut slope的真实候选与明确瓶颈

实际高坡度扫描 closing_highslope_tail_scan.json、脚本 closing_highslope_tail_scan.mjs
表明原wCut=.5并非绝对不能做低K尾。只需把capTransition从旧值2改成.05，
即可在slopeCap=.65时保持wCut=.5及其cut jets；这没有使用root后来设计的cut-preserving cap恢复函数。

两个更有用的实际背景：

| 参数 | 保留a=2.75候选 | 保持wCut=.5候选 |
|---|---:|---:|
| rCut / rCuff / width | .6 / .1 / .5 | .6 / .1 / .5 |
| delta0 | .1 | .1 |
| a | 2.75 | 4 |
| wCut | .1 | .5 |
| curvatureBound | 5 | 5 |
| slopeCap / capTransition | .65 / .05 | .65 / .05 |
| 实际重分配alpha | 3.228915143877657 | 3.085178498928804 |
| 最小所需径宽 | .436892285758934 | .441574685910332 |
| 实际高度增量 | .080349963975318 | .114267830495979 |
| 实际经线长度 | .511721997562743 | .520231582755088 |
| m2真实有限深线性DN，1024步 | 5.135447235156363 | 5.199985659013928 |
| 线性化Hθθ正性幅度阈值（采样） | 2.5632311297e-5 | 8.2241176949e-6 |

配置和输出分别为
closing_tail_r06_d01_w01_k5_p128_candidate.json,
closing_tail_r06_d01_w01_k5_p128_port_m12.json,
closing_tail_r06_d01_w01_k5_p128_amplitude.json；
以及
closing_tail_r06_d01_w05_a4_k5_candidate.json,
closing_tail_r06_d01_w05_a4_k5_port_m12.json,
closing_tail_r06_d01_w05_a4_k5_amplitude.json。

a=2.75候选将protectCell从80增加到128，数值DN与几何预算在本次浮点不变，
但无限深背景的保守连续曲率界由N80的52.38改进到N128的.019857
（尚需引入深cell校准alpha_n∈[.5,2]的统一界）。
a=4版本深尾背景界已经极小，但改变指数后的精确非线性存在/选线结论
不能自动套用原R20/R520文章。

新增已写完整证明的径向图全点对引理：
2026-11-09-closing-radial-reach.md。
母线切线锥角≤atan c、曲率≤K给
R_m≥(1+1/sqrt(1+c²))/(2K)；
旋转图任意两点法向弦长比≥min(R_m,inf 1/|κ_theta|)。
rCuff=.1,c=.65,K5给尾+平帽所有内部点对≥.18349016，
高于D≤5.2所需.156。不是对完整闭曲面reach的宣告。

原constructor末端buffer的实际K界有显式二次多项式充分条件，
不能由raw bufferMaxCurvature粗统计是否超K判断。
a4,w.5候选的该二次式最小值约1.773；向不利方向舍入后仍>1.7。
公式和所需区间包络均在上述几何笔记；相关计算
closing_tail_r06_d01_w05_a4_k5_bounds.json、
closing_tail_r06_d01_w01_k5_bounds.json、
脚本 closing_tail_radial_bounds.mjs。

**仍未能承接可见幅度。** 真实profile重分配破坏了原脉冲抵消，
并非给出true DN后就能把现有prefix的约.0037非圆高度接入。
a4候选的最坏位置为cell10 valley末端(r≈.10004358,w≈9.02e-18)，
a2.75候选最坏位置为cell0 transition5前段(r≈.5348,w≈.001386)。
这些是线性分支诊断，不是全局不存在结论，也不是非线性存在上界；
但当前“小扰动正性”证明不能承受现有幅度。
下一实质步骤是重校有限浅cell或在prefix提供更强衰减，而不是再次调整同一个synthetic Robin。

closing_tail_amplitude.mjs派生自同会话root_cut_tail_linear.mjs，仅替换真实constructor。
所有child脚本现在通过closing_tail_sources.mjs优先导入完整checkout的相邻题源码；
可用CLOSING_TAIL_CACHE指定只读缓存；导入前核对九个Git blob，
因此独立rerun不依赖当前scratch绝对目录。
