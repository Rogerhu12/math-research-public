# 原 P 全152低核、同源截面读者与完整两图除子

2026-11-20。独立实现契约；没有数学执行，没有改变当前运行源。
对应完整理论为 R925§23。实现仅处理当前 r=29 的原六个 P 端点；
不以此声称 mixed F、四大交除子或原 shadow 已经完成。

## 1. 从真实原上下文恢复全部核

`build_original_low_p_complete_kernels` 接受真实的
`rank2_original_map_section_fractions_context`。
原执行入口仍须先鉴定 F/P 两份完整特征零 PASS；其同源 RR、
原 QY germs、原二次常数域和 omega 已由原 map builder 支付。
读者不把布尔状态或短展开另当作原映射存在性的证明。

实际 P 权为6，对应完整 R3 基维数528。读者逐字重建
`solve_packet` 的整个1226×1056原系数矩阵：左半是 Q·A，
右半是 −QY·B，全部原列和已付全局零界均保。
在原常数域 k=F_(29²) 上求完整行阶梯形，所有152个自由列
各产生一条核基。实际接受门包含：

- 每个原系数行与整核矩阵的乘积为零；全部自由列构成152单位阵。
- 来自完整原矩阵的秩与自由列数相加恰为1056，核维数确为152。
- 两个528列投影均秩152；分母不是某个不完整子空间。
- 第一自由列所给向量与旧 context 已选原 N/D 逐坐标相等。
- 第三 embedding 的整个原矩阵等于第二个的真实常数 Frobenius，
  整个核也按同 Frobenius 运输，并对回第三原 QY 的全部行。

原有理 embedding 从 F29 扩到同一个已定 k 不改变核的完整性；
这里没有另选二次域、另取 omega 或把常数 Frobenius 当作 Artin。
每个 vnew 也逐值对回原 local packet。r=41 不在本实现的接受范围。

R881 的完整零界把每个已返回的核行识别为真正的 A=Y_i B。
所以这些完整分母恰为 H0(L³−Pole(Y_i))；R925§23 的
h0=152>g=85、deg=236≥2g 证明给全局生成性和真实极次数376。
不是通过有限次局部试验猜出共同零除子的次数。

## 2. 一次形成完整原 recipe 的线性读者

每个 j=1、4 的实际120条 M2 拉回坐标已在原 embedding 中：
它们是真正的 π_j*f_i/J，含原对数微分因子 j。
读者只用这些原坐标及同一个完整306乘法，形成每条 R3 recipe
的真实三因子乘积。共享的 recipe 前缀在这次构造中只算一次。

由原基权 d_i，完整权12坐标的位置为

\[
\{(i,a):0\le i<306,\ 0\le a\le12-d_i\}.
\]

每个真实 recipe 乘积的所有这些原 k 系数构成有限域矩阵 Q_j。
每个乘积已核权界，所以此展开包含全部坐标，没有隐藏的高次尾。
若 C 是任何一组原 R3 截面系数，C Q_j 就是这些同源截面
的全部加权坐标。将它们按原多项式环重新装回，并逐系数返回。
这只是 k 线性组合的准确重排，不是另选同维空间或拟合截面。

每个基础因子都已含 j，故三因子实际倍率是 j³；不得再丢掉
或重复乘该倍率。另一图一律通过原
`section_infinity_coordinates(value,3)`，沿同 J/J0 转换。

该读者避免对152个稠密组合重复展开同样的全 recipe 产品；
完整矩阵本身仍可能有计算成本，尚未实测速度或内存。

## 3. 实际端点配对分子和原函数身份

对同一原 embedding i，取原 λ_i=2/vnew_i，令

\[
N_\alpha=\lambda_i A_\alpha+B_\alpha,
\qquad D_\alpha=B_\alpha.
\]

全部 N/D 都是同一个 R3 截面空间中的实际元素，
Nα/Dα=λ_iY_i+1 是原端点 y 坐标。
第一条完整核行的两图坐标还须逐坐标等于原已选 map fraction
经过同 λ 组合后的坐标，随后两图都对调用者给定的实际
`OriginalFraction` 作完整交叉乘积恒等式。
因此返回的 `function` 是调用者的同一个对象。

调用者必须按 `row["original_embedding"]` 选择 i；
原 Artin 行序与 embedding 号不靠数组位置混同。
y0 使用原 j=1，y2 使用原 j=4。
当前六图的全部固定常数、原型和坐标同构均不改变。

## 4. 完整 A 理想、全曲线早停和全部余行

对同一个非空有序核子集，两个图和两个符号都取其所有原生成元。
一个生成元贡献的是完整306×306乘法矩阵的所有行，
每次更新都由既有完整 HNF 双包含认证；从不只取单个 R 行跨度。

R925§23 给这些同源截面的共同零除子是所需真实零、极除子
分别加一个有效剩余除子。两个图来自同一原子集并沿同一框转换，
所以它们粘成全曲线上的除子，不能拿两个任意理想仅按次数拼接。

每步读取有限图的全 k 长度，加另一图 s=0 的完整主分量长度。
后者可先从整个首一 HNF 行列式的最低非零指数准确读取：
对有限挠 k[s] 模，s-primary 的 k 长度就是 det 的 s 阶。
这里 det 是全部306个对角元的乘积，含全部剩余域次数与厚度，
不是约化 norm、一个小主子式或局部采样。

零、极两组的全曲线次数必须分别等于2256；若任一小于2256，
来源或计算已违反证明，立即失败。未同时达到目标就继续原下一行。
一旦两组均达到准确目标，剩余有效除子度零，两个完整理想已准确。
仍须逐一嵌入全部未处理的原 N/D，并在两个图核完整成员关系。
之前处理过的原行由每步完整 HNF 和单调包含保留。

最终仍调用原 `infinity_boundary`，取得真正的整个厚边界理想，
且核其长度等于前述 det 最低指数。只有两符号的有限加边界长度
均确为2256后，才能返回完整 schema：

```text
function: 同一个原函数对象
charts[False/True]: positive, negative
charts[True]: positive_boundary, negative_boundary
positive_degree = negative_degree = 2256
records: 两图全源、全部核、原recipe、全部返回及边界回执
```

没有将 pole-only 记录伪装成 `complete_divisor`。
完整152维基的全局生成性保证数学上的终止性；
没有预设两行足够，也没有任意次数上限后判“无解”。

## 5. 精确接入范围

接口为：

```python
reader = OriginalLowPCompleteDivisors(actual_model, original_tools_by_chart)
divisor = reader.complete_endpoint_divisor(i, j, actual_y, label)
```

模型必须保同一个实际 embedding、affine context、原 k 和 omega；
两图的工具须是同一真实基与同一原306正规化上的认证对象。
可在独立入口中从真实截面 embedding 构造该原 FractionModel，
也可由完整消费者传入其现有模型和原函数。
本 helper 不制造一个声称已完成七椭圆式或四交除子的 context。

未来接完整 geometry 时，原闭点 registry 和两个 engines 保持相同，
把整个返回值按同一函数 id 放进原完整 cache；不能只注入极次数。
当前 `prepare_original_ys_geometry` 还没有这个接入，故已有公开运行
仍走它们钉定的源。所有未来公开前端必须把本 helper 与实际依赖
同时加入 host/producer 完整来源清单。

原 yF 的完整零极仍需其自身门，原四 E 的全理想、完整κ/厚度、
原Tate/Artin/18×9双轴也都不由P端点计算替代。
这份契约仅对应已写候选源码和静态核对，不登记新的数学 PASS。

审阅：root推导并实现，global全文核原矩阵/旧首向量、完整两投影及P2全Frobenius、同源recipe与全帧/两图、全部原A理想/2256两符号早停及余行回代；只有AST与源码核对。源码SHA256 `80ecda38f71805cbc40394ca8b49bbc9ed3204325f832251d2b495d08aef4f79`。

## 6. 独立六端点公开门及真实 P-only 输入

新增关键字参数 `endpoint_section_fractions`。默认调用仍要求原
embedding 的 `F_and_P_fractions_built=True`；若显式传入六个原
P pair，则允许来自 `with_map_fractions=False` 的真实基础嵌入，
不修改其 certificate，不填不存在的完整 F/P 或七映射 context。
显式输入必须准确为 i=0,1,2 与 j=1,4 的3×2组，每组为原 R3
双图306坐标、真实父环和共同框位移12。完整核第一向量的双图
向量恒等式以及给定实际函数的双图交叉恒等式仍在主计算中逐项验收。

独立 producer 先认证同一 F/P 两份完整特征零 PASS，再重建原
map_sections（原基窗1429）、原306正规化（q2453/batch64）及
同一个 fast adapter。只从真实基础 embedding 的
`section_coordinates` 和 `same_degree_fraction` 构造上述六对；
每个实际端点为 `(2/vnew_i)*pi_j(Y_i)+1`，用真正的
OriginalFractionModel 与两个认证的原 chart engines/normtools。
P2 的所选系数与双图全部坐标另核 P1 的常数 Frobenius。

随后调用本件完整152核读者，每端点两个符号必须分别2256，
全部余行两图返回，最终实际无穷边界理想与有限理想的总长度一致。
六项全部通过才给本独立门 PASS；原 Y 上 F 分式、cube、四 E、
全部交点及 shadow 的完成字段仍为 false。原完整消费者和此前
运行仍保持原来源，本接口不向其 cache 注入未认证对象。

host/producer 的显式清单均为同序30源，实际依赖全部列入；
原读取器只在 host 收到只读令牌，数学容器网络关闭且源码只读。
请求固定 r29/q2453/batch64/minimal、同一 Sage10.6 镜像与原
F/P run/job/source/result pins。新 workflow 使用独立 concurrency
组、不取消旧运行、360分钟上限，只由本入口五个源路径触发。

当前 helper SHA256 为
`e289165044a280cedb47910b6ca7893942a25b19a8116f06662f803e62bd65bb`。
root 全文核四前端与完整返回，global 核真实 API/传递依赖及参数增量，
theta 核 full152/两图/函数及输出范围；全部仅 AST/JSON/YAML/源码检查。
实际公开执行及其 source/run/job/hash 另记 R925§25.1，不能由静审预填成功。
