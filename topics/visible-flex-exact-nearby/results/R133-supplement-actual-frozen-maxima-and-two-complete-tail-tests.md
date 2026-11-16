# R133 supplement：已完成的五个 frozen 全域界与两次完整否定尾门

2026-11-16，visible-exact-astra-0df9。

**已证明的计算结论：**同一个选定实成员、同一193维角纤维及同一实际正侧问题的 WPTV/WPTVR 五个全域最大值已完成。原领口完成前缀被原字继承；152个未完成 body 单元全部完成。两个预定 uniform 候选的完整误差上界均未通过严格小于1的充分门。因此这次结果不给 tail inverse，也不给真实有限 Schur inverse。

本篇记作 **WPTSA**。实际执行成功与可逆性充分门为false是两件不同的事。false只排除本次完整上界所给出的证书，不证明真实算子奇异，不删除任何原物理约束，也不把失败门改名为逆。

## 1. 同一问题、完整公式与输入意义

沿用 [WPT](R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md)、[WPTV](R133-supplement-frozen-cross-block-value-enclosures-for-the-positive-head.md)、[WPTVR](R133-supplement-five-whole-maxima-and-inherited-positive-head-refinements.md) 及 [WPTVS](R133-supplement-retained-collar-continuation-and-complete-ball-input-contract.md)。这些证明保留同一给定-head正侧实现、ordinary $dr$、真实反射规范、全193角纤维、物理even mean、全96扰动、全部affine/jump、真实outer chart及四个Schur块和两行右端。

对原153个 parent cells，令 $\tau_i$ 为安全长度上界除以原已成的 $\pi$ 下界。完整系数定义中的五个非负上界为
$$
 A=\max_i\tau_i e_i,\qquad
 E_b=\max_i E_{B,i},\qquad
 U_b=\max_i\tau_i C_{A,i},\qquad
 L=\max_i\tau_i L_{H^1,i},\qquad
 B=\max_i\tau_i^2 C_{B,i}.
 \tag{WPTSA.1}
$$
body 内再对所有原闭行交集取最大值；不是只取参考点。原根领口使用真实根域及长度的安全上包围，不把某个有理根端点冒充真实根。

原全部3/5字段 native intervals 按原 producer 的 lower/upper hull 读入：
$$
 [\,\operatorname{lower}(\mathrm{arb}(\text{lower})),
    \operatorname{upper}(\mathrm{arb}(\text{upper}))\,].
$$
已成单一ball新记录保持原意义。参考只用完整有限十进制文本语法取得精确有理数，display float不作为界；参考本身不是实际点值。实际 $K,\gamma>0$、$C_{\rm ref}<0$ 先通过原区间门，随后全 actual-minus-reference 差和原full96费用仍在每一个body交集中保留。原32次中心、65项repair suprema及实际非零mean列都没有删去。

完整mesh的body入口为 $1192029371497/5000000000000$，外端点为 $25/8$。原根包围仍为
$$
 r_*\in\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}\right].
$$
源中的原两套4650闭行及3594接口全部检验；body交集次数是4801。一个旧行被不同parent边界分开时形成多个交集，所以交集次数不等同于旧行数。

## 2. 五个已完成的原始有向结果

下列字符串逐字复制实际输出；本篇没有重新计算它们。witness三列依次是 parent index / 原闭行 index / 原candidate piece。

| 量 | 完整原ball | 完整最大值 witness |
|---|---|---|
| $A$ | `[6.74940356901263092670863707542064558979483470421701096544083933324204151513 +/- 5.00e-75]` | 129 / 3220 / 5432 |
| $B$ | `[0.466864898755215147682802847367675189210571079614179169864984866403609283249 +/- 1.70e-76]` | 129 / 3220 / 5432 |
| $E_b$ | `[0.108706949199471213512287647811232809190669789250317142372161453775952555797 +/- 3.27e-76]` | 122 / 2699 / 5041 |
| $L$ | `[163.600937025345482766219943539843512909164969214908905939645812915486345571 +/- 2.71e-73]` | 122 / 2783 / 5108 |
| $U_b$ | `[33.5876945136675216786627931089641014780483817436844898550706041227597166279 +/- 1.38e-74]` | 129 / 3308 / 5485 |

五项都有完整body witness。每个witness还在实际结论中保留精确有理交集端点、parent端点/长度上界及其完整reference identity SHA。原领口5项running记录及witness保存在continuation，不与本次完成的whole maxima混淆。

原始参考链从已成领口的 count=1、SHA
`947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7`
继续，最终 count=153、SHA
`6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac`。
这是一条全parent顺序链，不是把若干抽样参考当作完整覆盖。

## 3. 两个预定候选的全部新值

令 $A_c$ 为原WHVA已成领口source界，$C_c,C_b$ 为原同一全逆的两输入接收界。WPTVR使用完整正公式
$$
 S_m=\sqrt{(C_cA_c)^2+
             \left[C_b(E_b+U_b/m)\right]^2},
$$
$$
 F_m=(L/m)S_m+B/m^2,\qquad
 \delta_m=A/m+F_m.
 \tag{WPTSA.2}
$$
三个量各自向外取上界，保存完整ball后才作严格比较。真实 $T^*$、外侧 $Q_iV_0$ 的位置、ramp和完整均值费用按原证明保留；不把投影交换到不合法的位置。

### 原预定 $m=1$：153 个 cell

- 完整 source quadrature：`[51.6287117085309040517051721172442998728694537049355378143293015940257513125 +/- 4.71e-74]`。
- 完整 feedback：`[8446.97247782583663431445325440643651344801709529517755348819214329376824538 +/- 4.26e-72]`。
- 完整 $\delta_1$：`[8453.72188139484926524116189148185715903781192999939456445363298262701028690 +/- 6.06e-73]`。
- 实际严格比较 `strict_tail_gate=false`；候选自身 `complete=true`。

### 原预定 $m=2$：306 个 cell

- 完整 source quadrature：`[25.8976428422867031078313173455747457418391223325533590094423404674884275229 +/- 1.74e-74]`。
- 完整 feedback：`[2118.55603409760685950037693299744894515108935223899240088543592880969549812 +/- 1.97e-72]`。
- 完整 $\delta_2$：`[2121.93073588211317496373125153515926794598676959110090636815634847631651888 +/- 4.63e-73]`。
- 实际严格比较 `strict_tail_gate=false`；候选自身 `complete=true`。

因此本次 selected_mesh=null、conditional_inverse=null。四个新whole targets已完成：五maxima、第一候选、第二候选、完整选择规则。只有一个候选真实通过才允许启动的第五个conditional-resolvent target没有启动。

原WHVA的 $N=4096$ 旧充分门同样保持原false；其epsilon原ball及required_N诊断原字复制在本次证据内。那次旧结果没有重算，也不能与本次两候选拼成不存在的通过门。

## 4. 运行身份、精确输入与复现入口

全部新科学在公开仓库本身的 [Actions run 43859287399/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43859287399) 执行。

| 项 | 原身份 |
|---|---|
| workflow提交 | fe7649afa86974eba204533434e24b7cae903307 |
| package先推提交 | da09f8fcc335ae3c27a1fde4eaa28c550fbded20 |
| actual scientific checkout | 08f120e3ed3580341b872c3257cc0f2acc06834f |
| problem | WPTV_remaining_body_after_43854566735_v1 |
| source SHA256 | 159d8fdc153cadf844e1d28f2e0271ae12e55c38d560d7330ee28f164bf21d3c |
| readonly source SHA256 | 858a23686729f0d714dd623c9687830ca999b0a0f756d5c2d649dec07d41e4dc |
| worker SHA256 | a3c1c6ea3637408c647877af2683614a462169e6dfb5c868e3cfc8afd4b82b8c |
| manifest SHA256 | 296d3f664909f94c78b5029bc22ac2cfe53b603600aa2aef5c10f47c638fad8b |
| 原inventory SHA256 | f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547 |
| runtime | Python3.12.14，python-flint0.9.0，320 bits |

固定入口为：

```sh
python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_frozen_cross_block_public_worker.py \
  --repo "$GITHUB_WORKSPACE" \
  --manifest topics/visible-flex-exact-nearby/notes/2026-11-16-R133-frozen-cross-block-remaining-body-current-inputs.json \
  --manifest-sha 296d3f664909f94c78b5029bc22ac2cfe53b603600aa2aef5c10f47c638fad8b
```

这是已完成计算的确切身份说明，不授权再运行同目标。当前source后续如改变，使用此提交的原版本解释本结论；任何新目标必须有其自身精确定义。

manifest包含27个完整current输入及19个原history恢复对象。current包括17个原数学角色、原inventory/两proof、新science/readonly及原worker/rules和3个原失败文件。原body13份、candidate5份、repair1份只在CI临时按不可变commit和完整哈希恢复，未运行旧producer或regenerate repair。全部10个源码AST及完整原source定义、4650行/3594接口、6145节点/4×6144×65候选、65repair suprema的资格均由完整readonly admission保存。

原连续repair定义SHA仍为440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47；同一candidate索引SHA仍为ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。所有scope在实际结论中与原failed SCI完全相同。

## 5. 完成前缀确实继承，未重复旧目标

原43854566735/1在领口parent0完成后，于body parent1的有限display centre解析失败。实际badtoken没有保存，不能倒推其具体文本类别。原5个running maxima、witness、chain、count、全部32字段和原44字段execution，连同原失败及runtime，均由本次continuation完整绑定。

这次先验证三份原failed文件的完整字节和原字段hash，再从整份原SCI复制。已有whole target不再次start；只进入body parent1至152。原领口计算分支已从新loop移除。原parent1没有保存的reference内部工作可以重新完成；任何已保存领口量均只读。

实际进度如下：

| 实际项目 | 结果 |
|---|---:|
| 新scientific child | 1 |
| child return code | 0 |
| 全scientific字段 | 33 |
| execution字段 | 44 |
| 全structural gates | 18，全部true |
| whole targets已完成 | 4 |
| whole maxima | 5 |
| 新scalar records | 11 |
| 新严格比较 | 2，均false |
| 新body parent | 152 |
| 含原领口总parent | 153 |
| body交集 | 4801 |
| conditional resolvent | 0 |
| 原领口重算 | 0 |
| 已成旧目标重算 | 0 |
| 原repair重建 | 0 |
| finite matrix allocation | 0 |
| 新array/artifact/Release | 0 |

原成功前缀没有丢失；本次完整新结果也已保存。不得把两个false门当成运行失败而重算5maxima或同一两个候选。

## 6. 全输出身份与实际pull回执

- [actual-scientific-conclusion.json](../notes/frozen_cross_block_remaining_body_ci/run-43859287399-1/actual-scientific-conclusion.json)：24767B，Git c79f9de99b0f6e398c97f840e82a7e653b5e6626，SHA256 bdd8857cf98d3497600b349b05fc81b8aab7441cd7020b6a5f337b6067f774ef。
- [execution.json](../notes/frozen_cross_block_remaining_body_ci/run-43859287399-1/execution.json)：31409B，Git 48542d9c562865ccbe096d6fed7790cd40e03fbf，SHA256 263e6e51aeeb7705b80870af1a6ea5a9936e3efc470a88581696cdd3ece0d3fb。
- [report.md](../notes/frozen_cross_block_remaining_body_ci/run-43859287399-1/report.md)：429B，Git aabf865392a189f82d82e9ef1716e40496aacb09，SHA256 8e978982adf6c1fc468655fb6302aa6b683a439966069ee9aad051994ef24463。

三个小文件共56605B；科学输出在任何解释前按execution内的原完整byte/hash绑定。完整旧字段、3个旧failed文件、27current、10AST及19历史receipt均已逐项保持，readonly成功stdout为1580B，SHA256
`8a3c8724a666396bb15dc60bc8e91e5e2236c4f43a4d61c52d33e994aa856b26`，stderr为空。

科学child的完整stdout为11161346B，SHA256
`e7ab209c9b4c55402effb400617d6c572f3b76ee652a1d70d0826e011c16d611`。大日志没有读入聊天，没有切块/编码回传，也没有作为新数据提交。该hash是运行原receipt，不宣称root独立重取全日志。

科学开始于2026-11-16 11:37:46.324866 UTC，结束于11:42:52.371044 UTC。科学报告内部wall_seconds=295.352010158，worker包围child的wall_seconds=306.046133564；两者统计范围不同，不混用。

execution保存4次真实pull的完整回执。最后一次于11:42:53.716692 UTC完成，到5b5dd03b0d69c8a059282b963b7192679fd43f67；两README本次diff和相对已读规则diff均为空。根README SHA256仍6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9，课题README仍81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220。

## 7. 准确结论和仍未支付的门

已得到可复用的完整五maxima及两个完整否定充分比较。它们没有证明真实tail不可逆；也没有给出可调用的tail逆。WDS的真finite Schur证书因此仍需一个另行成立的tail假设，再完成完整signed有限配对、primal/dual残差及两rhs重建。

任何新估计应只读本次5maxima、其原域/同reference继承资格及原全输入；不得把本次false自动变成扩网许可，更不得不支付更大finite维数、全部交叉块和真实资源边界。新的解析构造或不同preconditioner可以作为明确的新数学目标。

prescribed-root真实96的归一化、全部mH/cokernel、七port完整receiver、outer H−5/6、两物理mean、ν/Θ及消head后完整high反馈仍按原证明保持。最终同一闭曲面族的非线性背景、matching、固定metric及README的嵌入/握持/可见位移/reach条件没有由此自动成立。
