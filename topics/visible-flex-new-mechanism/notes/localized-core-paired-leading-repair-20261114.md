# 局部新核心的成套入口修复：同一新度量、紧支撑共同高度原函数

日期：2026-11-14。状态：纸面推导与独立源码完成；公开人工检查、唯一新初态实际审计尚待回执。没有调用本地研究几何或优化。

本设计接续 `notes/localized-elliptic-core-physical-field-transport-20261114.md`，使用 `results/R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md` 的入口公式。前一个局部 $B=.37$ 初态已完成公开运行 `43636741138`：它保住了外域全部二 jet，但局部误差仍约为 $1.185$、曲率样本峰约为 $270.7$。这些数来自 `notes/actions-43636741138-1-localized_core_initial/core-B037-localized-accepted-initial-summary.json`，不是本地重算，也不是严格几何界。

## 1. 哪个低阶条件没有随核心自动改变

设 $s_c=9/250$、$x=s-s_c$。旧核心为半轴 $(1,7/25)$ 的准确弧长椭圆柱，新核心半轴为 $(1,37/100)$。上一设计固定

$$
a_*(s)=a_{\rm old}(s)+\chi_{\rm loc}(s)(a_{0,*}-a_{0,\rm old}),
\qquad
d(s,\theta)=\chi_{\rm loc}(s)(u_{0,*}(\theta)-u_{0,\rm old}(\theta)),
$$

其中 $\chi_{\rm loc}=1-S_{11}(x/\ell_{\rm loc})$，$\ell_{\rm loc}=81/500$。开核心与外域取准确常值延拓。因为

$$
\chi_{\rm loc}=1+O(x^6),\qquad
a_*'=-Cx^3+O(x^4),
$$

这一操作更换了核心的零阶半径和切向角，却没有更换旧场固定的 $u_4,v_7,b_6$。

R64 的 $k=\partial_\theta\psi$ 是**材料角转速**，不是空间曲率。准确同度量入口要求

$$
U_4=-\frac{Ck_\theta}{4a_0k^2},\qquad
V_7=\frac{\sigma C^2k_\theta}{7a_0k^3},\qquad
B_6=-\frac{\sigma C^2}{2}\langle k^{-2}\rangle.
$$

原可变场的 $u/v$ 自由项分别从 $x^5,x^8$ 开始，独立高度自由项从 $x^7$ 开始。因此，仅开放原 162 个坐标无法改变它们锁住的 $U_4,V_7,B_6$。新旧 $U_4$ 确实不同：在椭圆长轴端点

$$
\partial_\theta U_4(0)=\frac{3C(A^2-B^2)}{4AB^2},
$$

对固定 $A$ 与 $C>0$，增大 $B$ 严格改变右式。这给出该有限表示的准确低 jet 失配，不是一个正误差下界，更不排除一般 $C^2$ 构造或可收敛的更大空间。

## 2. 保持完整新度量，成套替换三个系数

本次保持上一局部设计的完整度量定义逐字相同：

`211c1b193eeb38b50933083821b3d32ed8e7bbf6bd627aab64630dd8a6c22a5e`。

不更换选中的旧完整 $a_{\rm old}$，不以种子半径代替它，也不增加自由度量系数。新度量的正性仍由 $B_*>B_{\rm old}$、$a_{0,*}>a_{0,\rm old}$、$0\le\chi_{\rm loc}\le1$ 和 $a_{\rm old}>0$ 给出。

令 $\Delta U_4=U_{4,*}-U_{4,\rm old}$，其余同理。选独立修复宽度

$$
\ell_e=81/1000,\qquad
\chi_e(x)=1-S_{11}(x/\ell_e),\quad 0\le x\le\ell_e,
$$

并对带幂乘积采用区间外零延拓。对每个当前旧参数向量 $p$ 定义

$$
\begin{aligned}
u_*(p)&=u_{\rm old}(p)+d+\Delta U_4\,x^4\chi_e,\\
v_*(p)&=v_{\rm old}(p)+\Delta V_7\,x^7\chi_e,\\
\Delta z_c&=\frac{\Delta B_6}{7}\,x^7\chi_e,\\
z_{c,*}(p)&=z_{c,\rm old}(p)+\Delta z_c.
\end{aligned}
$$

共同中心速度随之定义为

$$
b_*(p)=b_{\rm old}(p)+\Delta B_6
\left(x^6\chi_e+\frac{x^7}{7}\chi_e'\right).
$$

这与直接加 $\Delta B_6x^6\chi_e$ 有实质区别：这里先定义同一个紧支撑中心原函数，因此总速度修正的积分准确为零。修复端之后 $z_c,b,b_s,b_{ss}$ 全部恢复；尾帽没有累积高度平移。

新固定高度参考为旧 $b_0+(\Delta z_c)'$。它是**新的 $b_0$ 身份**，不继承旧参考的全域 $|b_0|\le1$ 声明。九个可变高度列保持原来的准确基函数、原函数和参数语义；它们没有被重新拟合。$\Delta B_6$ 的数学定义始终是两个完整材料圆周积分的差，固定角网格只负责数值评价。

## 3. 闭合、两端、外域与适用范围

新的固定 $u$ 修正是 $\pi$ 周期奇函数，固定 $v$ 修正也是 $\pi$ 周期奇函数。配合旧空间的对称性，$T_{xy}$ 在 $\theta\mapsto\theta+\pi$ 下变号，$T_z$ 在 $\theta\mapsto-\theta$ 下变号。因此逐圈 $\int T\,d\theta=0$。不需要、也没有声称整个三维 $T$ 都是 $\pi$ 反周期。

位置采用原来的零均值规范

$$
X_*(p;s,\theta)=a_*(s)\Pi T_*(p;s,\theta)+z_{c,*}(p;s)e_z.
$$

开核心上 $u_*=u_{0,*}$、$v_*=0$、$a_*=a_{0,*}$，共同高度仍是 $\sigma(w+s)$，所以端口是准确的新椭圆柱。所有新增带幂项在入口灭至少三阶，S11 在修复右端也足以保完整位置二 jet。

对 $s\ge s_c+\ell_e=.117$，新场恢复为**同一参数**的上一局部设计；对 $s\ge s_c+\ell_{\rm loc}=.198$，恢复为**同一参数**的旧全局模型，包含 $X,X_s,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta}$ 六项，而不只是速度。关键是同一 $\Pi$ 规范与紧支撑的 $\Delta z_c$。

“同参数外域相同”不表示优化以后外域永远等于当前 $f198$ 数值状态：当前 $u/v$/height 参数一旦变化，其对应的旧模型也变化。这给未来联合优化一个可追溯的可变族。本次只审计原 $f198$ 系数的一个初态，不优化。

修复只支付已识别的 $U_4,V_7,B_6$。它不保证新 $u_5,v_8,b_7$ 或更高 Cauchy 系列，不保证本次有限宽度 $0.081$ 已足够小，不保证最大度量误差、曲率或共同高度改善。尤其原外域的镜像法弦缺口与尾补丁曲率仍会保留。

## 4. 参数导数与身份

新增固定项不依赖当前参数。原 $u/v$ 基函数及其 $s,ss,\theta$ 导数保持原列，仅在新的完整 $u_*,v_*$ 上重新计算单位切向 $T$ 的链式导数。通过同一个 $\Pi$ 得

$$
X_p=a_*\Pi T_p+(z_c)_p e_z,
\qquad
(X_s)_p=a_*'\Pi T_p+a_*\Pi(T_s)_p+b_p e_z.
$$

二 jet 的参数导数使用相同乘积规则。高度列仍是其准确原函数 $I_j$、速度基 $C_j$ 和 $C_j'$；没有把新的固定中心修正计入当前参数 Jacobian。完整 $g_*$ 固定，因此没有半径参数列。

`scripts/frame_localized_core_entry_repair.py` 提供 `LocalizedLeadingRepairProblem`。它保留原 162 维坐标，不增加 $Q$ 列；`source.space_definition` 明确包含新核心与固定修复；`metric_model` 沿用已发布局部度量；`height_base_definition` 则升级。永久原 $c_0$ 来源与当前初态 $f198$ 来源分别保留，彼此不替代。评价角数、共同高度求积规则和新的 $\Delta B_6$ 材料均值角数都只在评价身份中记录。

## 5. 唯一初态审计与人工范围

`scripts/frame_localized_core_entry_audit.py` 严格回放原四个公开输入，取 accepted 九高度状态

`f198ba74dcf3644569bf1ed78eecbc48a0f21ec421205d46a6b159cb00ff0f56`。

在同一个结构网格保存旧参考、已经发表的未修复局部场以及唯一新修复场，三者只是为分离来源的只读对照。新候选只有一个；优化器和高度提案调用数均为零。完整径向节点含旧入口、局部支撑与本次修复支撑的准确有理分点，角数为 384，再固定同一状态评价 768。

保留完整二 jet 端口、$E,F,G$、实际曲率、镜像点对、球/条带、R66 新 $B=.37$ 帽高门、共同高度和 $b$ 极值；单列修复区与剩余局部区。稀疏端口查询与完整查询共享原固定 prefix，加同一个显式 $\Delta z_c$，不按查询网格重新积分。保存完整报告及带字节 SHA 的紧凑 summary；任何输入失败仍保存小回执。

公开人工检查只用 $A=.9,B=.72\to.8$ 的已声明小载体。覆盖完整参数二 jet Jacobian、新共同中心三阶径导、core 端口、原与扰动参数的外域恢复、稀疏/密查询、评价身份、freeze、完整四输入主流程和错误 SHA 拒绝。未运行的检查不会记作 passed。

## 6. 公共命令

```sh
python topics/visible-flex-new-mechanism/scripts/frame_localized_core_entry_audit.py \
  --check-only \
  --out "$RUNNER_TEMP/localized-leading-development.json"
```

公开人工成功后，唯一实际初态为：

```sh
python topics/visible-flex-new-mechanism/scripts/frame_localized_core_entry_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --out "$RUNNER_TEMP/core-B037-localized-leading-initial.json"
```

实际分支必须是 `Rogerhu12/math-research-public` 的 GitHub Actions，输入位于本课题 `notes`。没有本地真实核心构造或候选评价。
