# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话Astra-held10-f00f08c9-20261117。**进行中；尚无满足全部完成标准的候选。** 详细旧结论/失败保存在notes、results和log，不重做。

## 目标、规则、同步

连通闭曲面连续C²等距嵌入族；固定有内点闭H、diamH≥.2D；整像δhold≥.1D，含反射取商δE>0，全时reach≥.03D。固定同一g/物理参数/时间范围metric≤1e−6且加密下降；材料位移或solver success不替代。

- 已部分克隆、真实pull并全文读根README授权/全部规则及本题README。
- 已读规则提交：`ababf2529629665d00d13114848a6bcc08ce1458`。2026-11-18 03:52:54（UTC+8）独立稀疏发布worktree真实pull后双README无变化；至少每小时pull，变化只读diff并立即执行。
- 每结论更新H并发布；非快进即真pull --rebase再推，禁force。终端无认证，已连接GitHub接口按根8作每文件<100KB小文本原子提交；仍终端真pull。
- 可重算数组/mesh/checkpoint不入Git/Release/CI artifact；保留脚本/命令/参数/hash及标量。H<10KB、单Markdown<100KB；无根LOG。达到完成标准后继续提高比例。
- 原工作树供agent写源；独立publication树负责Git，避免autostash竞争。旧scratch只读。主会话独占Git。

## 1. 当前主线：n4局域圆弧与实际尾

R19/19A固定圆弧逆刚体换握持：中心对称整像的Hausdorff位移≥实际圆心平移；中央柱长.54付H直径，固定二fold帽排O(3)。圆心、全径比、reach、真实闭合必须逐项支付。

**大rho精确核心**：eta1、轴π/4、a=.147/b=.08，C4局域修平加全局均值补偿；β∈(−2.437434179108102,−2.437434179108101)，|c|/q∈(47.53249652612922,47.53249652612923)。q.02/.022时R1.9/1.99、零控制rho>.50125/.45137。若完整D≤2.65、σ≥.08、K≤12.5等，则held/D>.104902/.115401且reach/D>.03018。alpha=2Ra−.001、ell=.54；实际大R的Rvu<1及初负K保护窗已付。未来补弧控制须重付rho；前缀/尾/闭族仍未付。见n4-large-radius-circle-core与纯Fraction脚本。

**低eta选择已实算**：真实圆心系数随eta仿射，eta.1/q.049给零控制rho>.234093、条件held/D>.103812，所激发mode8约eta1/q.02的四分之一。六个已知物理根只做新沿程诊断、未重搜：mode8中段放大约10.20–14.17，线性采样不是非线性界。见n4-large-radius-eta-selection。

**已实际联立**：n4 eta1/q001/M12 λ0，993节点。实际outer校正后物理BC3.8058e−14；最终tail res4.1448e−10/minA.99073/metric1.11e−14；mean两jet差1.30e−13/−3.04e−12，非mean二阶1.70e−11。prefix metric1.1175e−7；仍低幅/未圆化/无闭图。见n4-first-true-coupled-state，源resume_n4_tail/couple_actual_tail.py。此前q005/eta*/M8的首实际尾响应仅单独接口，不冒充联合。

eta.1/q.01/M16 λ0前缀已接受724点，metric2.38461e−8/tensor1.62253e−5/K6.51157/rootmargin.00394505；δ=.030027177128287334、vd=.24836306559053845，仅线性port。见n4-eta010-amplitude。主会话正在原N512/parts8/RK16真正联立；n4 agent推进该eta增幅、eta1低幅圆化和固定g入口。保持原2e−9 tail门及D/S/A条件。

旧n4设计与正根域/maxnodes/取消均见bimodal-continuation-terminal、n4-q*、double-prefix-*；delta/vd重解不是同g。q06采样K15.954给reach/D必要上限.02949，尚非区间证书。vu.4双根τ12≈−.6587，旧有限圆化完整metric未过；不重做。

## 2. m3真正联合与新物理尾

**原固定g**：δ=.06105607686781097，g SHA11a9…b125。q02 M8→M16/parts8过原门，M16 tail res1.161e−9/minA.440917/fullD2.735e−7。固定g径向983→2462点使prefix metric4.971e−9→5.845e−11、tensor9.015e−6→1.947e−6。见m3-fixed-m16-parts8-and-radial-floor、m3-true-radial-refinement。

恢复旧q021/q025而未重算：q025 δ=.06105528571325212、prefix metric3.690e−9、tail res1.857e−9/fullD4.422e−5/minA.26267。q026/RK32终态2.613e−9、q0275几何初值+局部同伦3.375e−9均未过2e−9；含startup失败7条记录见m3-finite-continuation-initializers。

**新beta3.625**：仅首谷控制改变，其余控制参数不变，但全局重标定改变整个r(x)，故是新g。q.02接受后q.0225已完整联合：δ=.061055703925903294、936点；prefix metric4.53177e−8/tensor7.15029e−5/K8.13283；tail res1.37881e−9/minA.618156/metric2.03136e−9/fullD1.81912e−5，物理BC1.25159e−10。不同q仍重解δ，不称同g；见m3-beta3625-second-coupled-state。

beta3.625由q.02/.0225 secant到q.025：原shoot终态2.35394e−9；收紧局部root10倍后3.36278e−9，L2选步也停于该态，均未过原最终L∞2e−9。收紧后旧态首次重算3.2779e−7，保留局部误差放大，不把一次门通过当严格证书。见m3-beta3625-q025-stalled-continuation；现转beta4.125实际联合。

**新beta4.125/q.02已真联合**：δ=.06105607210171944，prefix metric2.88465e−9/tensor5.64731e−5；tail res6.17866e−10/minA.800809/metric2.52176e−12/fullD1.78152e−8，物理BC1.17789e−10。与beta3.625同q各自重解后的有限fullD改善158倍，非同g精化。见m3-beta4125-first-coupled-state；原数值路径继续q.025。

旧q025 H跨新beta初值：旧状态res175934、新线性态+旧非线性余项1.718e−8/minA.05537，均失败；全谐波线性三角和.72876→.43637不是非线性容量。原sameg守卫保留，先原port重启后显式切新g；cut仅记录64ULP舍入界。该失败态minA在stage40、残差峰stage46；stage44关键分量1ULP/scale=2.7035e−9已过门，不能据此放门或证无解。见new-first-valley-actual-start、tail-residual-and-positivity-locations。

## 3. 实际闭图、同g精化与连续metric

R21/R23构造有限M8共同Cartesian二jet/mean的完整C² S²，504320前缀盒+4637尾段给全相位σ>.7/K≤10/D<2.30242/reach≥.1。零marker时δE=0，精确等距未证；源finite_closure/m3_m8_*。

R24原M8非零固定帽证明全O(3)非全等，held/D>.00543686。R28新M16/64步图自身1261568前缀盒、新尾界、自身体积矩和固定帽给D≤2.301491469394、reach≥.1、H径比>.6979428、held/D>.00546265624、δE>0。三个惯性根互异及core cos3→sin3排反射；全帽内部查询一致，未移用M8矩/旧cut。见R24/R28。

**同checkpoint尾32→64步**：真实R处metric1.8282e−9→1.4441e−10；整面最大仅降至1.6485e−9，被未加密prefix主导。内部Vrr误差约降5倍但全尾两层二阶差仍.00629485，未证C²极限；旧差分步不是主因。每层重做cut/mean。见m3-closed-metric-and-rr-location、m16-same-checkpoint-radial64。

**R27原g真背景**：432段/10034叶的总变差、四阶区间Simpson和深尾余项给λ∈[161.87100490348996,161.8710049035018]；工厂λ严格偏高(2.0236e−11,3.2089e−11)，不能代替真g。closed_geometry正补部分积分/严格反函数与全角/全径向metric，不再铺低幅几何盒。源resume_closed/certify_background_sharp.py。

## 4. 已登记证明和另一高幅入口

R12/R14：h=g−dz²正定且同严格Q号时，高度二jet和g一jet确定刚体下Cartesian缝；mean转角/Darboux补二jet，Q0例外。R15反射轴曲率必要界；R16过零权无一致L²逆；R18完整mean/cos/sin混合DAE。R17非轴反射二fold不可套象限证书。

R20/R22单/双谐波到精确圆弧正距离，切空间障碍须完整核+可微支；有限共振不证不存在。R25固定Q/g的完整动量正A凸域严格单调、唯一根和残差界，不保证shoot存在。R26三谐波圆心半径约束minimax给n4/a.147/q.06弧差<8.433e−5、rho>.0999241，但第三物理核缺。

旧m2 smallcut同g q20 M20→24 metric9.93e−7→4.172e−9，q22 M28→32为1.133e−6→1.119e−8；仍线性DN。R11开放q20的843264盒给σ>.349674/norm<1.508969/witness>.3254827/K<8/held/D>.1076。R13若真尾rXY≤.35、顶高≤1.526541485、K≤10、σ≥.3并C²闭合，则held/D>.10338且reach/D>.03191；真尾尚缺。

m2旧补弧高M初值负rho不是无解；新首三谷[4.25,3.9375,5.0625]给mode2线性H阈2.11656e−4约旧3.08倍、DN11.85689844；65次真实重标定screen仅新设计，非非线性容量/同g。见mode2-three-valley-design。R1–R10、旧GC/短领失败与R114仍留历史，不重复。

m2循环方向/次数新线性screen已完成：外向两循环6根、内向单循环5根；保留实际H/q、背景采样K/尺寸与完整复现，尚无这些设计的非线性BVP。KD诊断不是必要障碍。见m2-loop-transfer-designs。

n4第三核两新物理搜索：最大半径插柱4初值、三个C³半径控制3初值均未得τ4/8/12共同根，含边界/次数/xtol终态；优化器成功不等于根，未证不存在。见n4-physical-third-mode-searches。

## 当前分工

m3_true_coupling：新beta实际增幅；n4_round_core：圆化/低eta增幅/固定g；closed_geometry：全域连续metric；主会话：n4真尾联合、物理传递设计、同步逐结论发布。完成一个子问题即接open.md，不以阶段结果或时长收尾。
