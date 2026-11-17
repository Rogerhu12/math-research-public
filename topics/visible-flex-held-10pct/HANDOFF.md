# HANDOFF — visible-flex-held-10pct

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

构造连通闭曲面的连续C²等距嵌入族，固定有内点的闭H，diam F₀(H)≥.2D；整像Hausdorff变化δ_hold≥.1D，含反射取商δ_E>0，全时reach≥.03D。同一固定g、物理参数和时间范围下，最大相对度量误差≤1e−6且加密下降。材料点位移不是δ_hold；优化success不是数学完成。

- 已部分克隆并真实pull main，根README（含授权）和题README全文已读。仅本题及其workflow稀疏检出。
- 已读规则提交：`223833352b25324a94839bd297db3a047d2f08bf`。2026-11-17 22:16:51（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 23:16:51；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每条结论同时更新本文件并普通push；非快进立即pull --rebase再推，禁止force。每次pull比较双README，只读差异；至少每小时一次。令牌只在命令行临时使用，不存文件。
- 只有完整证明进results；数值证据、条件假设与缺口分别写明。可重算数组/网格/渲染/CI artifact不提交，只存脚本、参数、运行ID/hash。单Markdown<100KB，本文件<10KB；不写根LOG。

## 主线A：小切口高振幅前缀 → 真实非线性尾

已将cut从旧r=.6移至r=.30，真实背景w=.08、w_r=−1.8666666667；vu=.55、vd=.60、flat ramp=.4、eta=.05、单环，ShortBridge curvature4、peak_fraction=.2。割线只改变初值，原Frenet/端口方程未改。设计延拓已到q=.22（q21/q22设计误差略高于1e−6，q22同g M32尚在算）。

固定同一物理profile/chart/port/warp的实际加密：q14 M14→M16，metric1.16e−7→1.16822e−9；q18 M16→M20，9.98e−7→2.42874e−8；q20 M20→M24，9.92e−7→4.17253e−9，actual q=.20000109659082244、κ采样6.62074、高度1.27654148、最小Frenet根5.64176e−4。以上均是开放前缀，不是闭合解，也无连续reach证书。

真实q20端口包含完整非线性均值，512角点2jet，SHA `0d03cd6128d7e498c28b60b2ea82c8ce4cd0af03d0e50bb1fc3cae8b54ee5355`。复现：scripts/recover_prefix.py与prefix_recovery_manifest.json恢复源；smallcut_prefix_sweep.py建立新chart，smallcut_secant_launcher.py延拓，fixed_refine_smallcut.py冻结g加密，smallcut_endpoint.py导出端口。精确命令/参数/hash见smallcut_delivery_manifest.json；完整表及失败路径见notes/2026-11-17-smallcut-high-q-and-fixed-g.md。所有数组仅scratch。

明确的共享二jet五次Hermite和s≤.04的解析core中心lift已支付有限表示及上下接缝C²；同g、同lift的M20→M24 metric 9.93076e−7→4.17249e−9（238倍下降）。外端不变。全Cartesian Fourier/Hermite表示已发表，纳入角图分段后同g M20→M24 metric9.93077e−7→4.17200e−9；其s≥.04主体已逐区间通过793600盒：σ≥.349674、半径≤1.508969、witness≥.3254827、8I±II严格正；独立审读通过，中心解析lift仍在核查（cartesian-tensor-prefix笔记）。修复后的全prefix X·n采样最小.352673、κ6.62074；中心对称整像D的mesh-cover估计≤3.030641，实际曲面witness下界估计≥.318244，比例>.105。仍是浮点覆盖预算，未定向舍入；不是连续reach/闭合证书。若尾rXY≤.35、最高z≤1.526542，则尺寸能容纳增高.25。详见smallcut-c2-center-and-geometry笔记与新增两脚本/manifest。

[R7](results/R7-twofold-markers-core-moment-and-geometry.md)已为二重对称闭族证明固定双帽的δE>0机制，给显式C² bump、曲率/面法线支撑界与当前q20核心矩Re A_C>.11262048876的有理下界；只在真实闭族/接口成立时适用。

真实非线性尾及共同二jet复核见scripts/nonlinear_tail、nonlinear-tail-stage1/common-twojets笔记。upper输入必须−H，再整体反射z。原深度160尾的M8支到λ=.0781（完整q18端口的比例）；λ=.07同g M8/12/16共同网格metric8.03e−9/2.24e−9/9.29e−10，但完整Darboux缺陷1.96e−5/1.15e−5/8.23e−6，Xrr层差.00382/.00130且差分步噪声仅4e−12，C²/无限尾仍未付。有限Gram延拓仅限固定M，不给穿零极限。新首cell宽脉冲/平谷的深尾保持，DN改变须重配prefix；两个代理现已接通既有真实DN联立器，从低q联合seed增幅，保留全均值与Cartesian两jet重验。

[R10](results/R10-exact-cone-annulus-through-zero-A.md)构造严格同g、C∞嵌入的局部锥环带，0<w≤.01/a≤.01/r≥.2全窗κ<.77且D,S>0；指定幅度下A真正变号。因此A>0是既有图的限制，不是一般几何必要条件。此环带仍须满足Hr=H/r、共顶点及完整两jet，尚未接上prefix/深尾。

## 主线B：精确圆弧核心与换握持

[R3](results/R3-rigid-arc-regripping-and-Hausdorff-amplification.md)已证明：实际圆弧局部片的phase是QαX+bα，对整个族取逆刚体运动使片固定，D/reach/g/δE保留；三重对称给整像dH≥√3|c|sin(kα/2)。R4的Fraction脚本严格支付四组核心/角窗/H直径/局部曲率支撑预算，例如R=.25、normal宽1.2、phase.14、D≤3.9给held/D>.10837、Hdiam/D>.21519。它们是条件窗口。

[R5](results/R5-degenerate-inlet-local-arc-uniqueness.md)用完整加权能量在精确C³前缀假设下支付退化入口圆弧保持和传播角窗，保留−M²Nu/N²项；不适用于任意C²有限插值。R6用三阶矩、三重标记帽和短中央柱证明有严格几何余量的精确族可获δE>0，包括反射；仍须真实前缀/尾。

[R8](results/R8-positive-band-circle-obstruction.md)由Ghomi–Spruck原定理严格推出：若精确圆弧旋转片真的进入完整正K环带，则周期性强制k为整数，嵌入强制k=1。R2核心k=.5和R.25核心k=4都受此条件障碍；但从K=0边界进入正K内部的退化唯一延拓仍未证明，不能据此宣称旧profile或本题不可能。正在保持H后增加负K段，以先耗尽R5已保证的保护窗，再解全BVP。

[R9](results/R9-consumed-circle-window-and-background-curvature.md)给已完全定义的新C³轮廓：保持s≤.42原g，额外加速.17→.38；首个正K带前特征损耗严格>1560443/1692724>.92>.9。末端r=.6/w=.5两jet不变；标准库Fraction/Bernstein证得旋转背景κ≤55/8。仅支付轮廓/背景；非圆全BVP、真实圆弧是否消失仍未证。

精确core lift旧profile：λ1/M4根metric≈.00805，同gM6未过；9858阶有限terminal Schur归一化条件数4.27e8，不给无限维存在。新loop保留R9前两段：非圆弧λ0基线固定完整g M4→M6 metric1.776e−9→6.393e−10、Darboux9.13e−8→2.65e−8；λ.3设计仍metric≈3.93e−4，λ.5控制饱和且失败。源码/固定参数/全终态hash见scripts/plateau与window-loop-actual-prefix笔记。未获精确圆弧prefix。该代理现优先适配既有实际非线性DN耦合器，保留全部均值/两jet与真实外层重验。

## 其他已测路径与复现记录

- 新短尾：旧r=.6 q20固定E metric≈.002；自由E曾退化且κ≈5.7e6，淘汰。有界E改进到metric=.00039991、κ9.95565仍不合格。新q17小cut首试发现G≥.005与cap=.05不相容；保留原默认复现，显式G-floor=.0005的dense重算因session中断无终态，不作数学失败；已从保存首试精确插结点至nc31/M12；分块稀疏Jac的100次新试验正常结束，metric=.000432458、κ10.0221，仍不合格（refine_collar_design.py）。见notes/2026-11-17-bounded-and-smallcut-collar-trials.md及short_collar_trials_manifest.json。
- 完整三场GC BVP已实现；B=.9 metric≈.0289、B=.7≈.444，低频/末端误差未消失，不接受。R2给GC系统与平面圆领两jet引理；见gc-complete-bvp-attempts笔记。
- 直接半帽20轮已发表源码/失败表；第三批宽包络最好metric≈.009869，真弧长规范仍.011277，均未过。R1温和椭圆给10.3%条件几何预算，连接器未实现。
- 厚尾固定160深度的选定参数/源闭包/复现入口已发表；height .0169206、新DN=11.902268、重新匹配H1/q=.0135088，首模线性诊断换算q=.0271956。它只是采样一阶正根窗口，不能当非线性容量界，见thick-tail-linear-coupled-diagnostic笔记。旧大cut q18 M16已核固定g误差2.55e−7，M24主动取消以优先新小cut；非数学失败。
- 本题独立workflow `.github/workflows/held10-smallcut-research.yml` 的8参数Actions [44084871328](https://github.com/Rogerhu12/math-research-public/actions/runs/44084871328) 已结束并核全8份日志；最好r.35/桥3.5/p.1到q18，仍不如本地主线，失败均为所试粗延拓路径而非几何上界。精选标量/hash在ci/smallcut-run-44084871328.json及Actions结果笔记。最多2并发，不上传可重算artifact。dispatch曾403，按已授权普通push触发。job success不代表数学成功。

## 来源核对与当前交接

历史来源R114/flat17约held/D>.0527832、reach/D>.0312033、metric≤1.2567e−9，仅作来源结果；旧约.063为未解暖场。前缀是主要尺寸成本。源复现与文献核查见开题笔记，不将来源结论冒充本题独立验收。

主会话负责规则/证明复核、直接新尾、整理与逐结论push；三个并行任务如上。全部未决验收见open.md。当前没有满足10%的闭合族；继续实际尾/前缀并核全时几何，达到后继续提高比例。
