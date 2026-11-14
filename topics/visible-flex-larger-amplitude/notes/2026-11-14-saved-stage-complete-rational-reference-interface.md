# Actual47 四级矩阵：完整有理参考与候选比较接口

本入口只消费 actual47 已保存的四个完整局部矩阵、原 h/port、两个旧矩阵及三个原输入方向。它不重新调用 RHS、root、局部 J、ODE、native solve 或 nonlinear trial。全部科学运算只能在 Rogerhu12/math-research-public 自己的 GitHub Actions 运行。

源码为 [exact_20261114_saved_stage_full_rational_reference.py](../computations/exact_20261114_saved_stage_full_rational_reference.py)，37,047 字节，SHA256：

119864f3dffd764500e3f15b9bfe8c7e27367384486eaaa11a5db885422b8f12。

已执行的本地检查仅为完整源的 AST 语法解析；未 import 该模块，未执行参考矩阵、数值比较或任何科学运算。下述接口不是实际结果。

## 输入对象与身份

入口锁定实际47捕获 result SHA：

da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403。

冻结 reader 为 [exact_20261114_single_step_rational_action.py](../computations/exact_20261114_single_step_rational_action.py)，SHA256 9c42982291bd1a7b7cf21c472d8aae877136fb884708a8310ca6bb882c1d103e。该 reader 对完整21数组、原三份capture源码、固定metadata、原 h/port/sigma 进行原有校验；只导入读取和精确运算定义，不导入或执行 native producer。

同时锁定实际47三作用 result.gz SHA：

f145cf0efea702964413abf5490df5f2ef584b373afb9b8213f001774e9ea33b。

三份 case 与完整1792字节输入分别逐文件核查，原输入为 Q112 单位向量、Pi112 单位向量、actual43 最佳方向的原节点520。后者沿实际47已完成的9c读取路径绑定原43完整方向/checkpoint；本入口不重新下载43大包，不重构或阈值化方向。三作用的完整 input-binding 须与当前捕获一致。

可选候选由 [geometry_20261114_saved_stage_rk_covariance.py](../computations/geometry_20261114_saved_stage_rk_covariance.py) 先形成。当前冻结SHA为 01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548。消费者要求显式实际 result SHA 与源码 SHA，核当前源码字节、结果/manifest来源、completed标志及共有capture绑定。候选schema为：

saved-four-local-A-R271-frequency-balanced-RK4-candidates-v1。

数学输入只取 candidate_maps 中两个完整的 little-endian binary64、C-order、形状 [226,224] 的原坐标矩阵：

- r271-frequency-balanced-longdouble；
- direct-original-coordinates-longdouble。

两者已经付原出口Pi port。full_original_output 主别名及其 shape_J/mean_rows 切片须逐字对应完整矩阵。其余工作longdouble数组只按原descriptor完整核字节、SHA和声明dtype，绝不误作binary64解析；实际精度、x87有效字节与padding由候选producer另存。

## 完整参考的有限定义

令 $K=224,R=226$，$A_i$ 为这次保存的 $R\times K$ binary64数组按原二进制值解释的精确有理矩阵。对每一个输入列 $e_j$，依次形成

$$
k_1=A_1e_j,\qquad
k_2=A_2(e_j+\tfrac h2(k_1)_{\rm shape}),
$$

$$
k_3=A_3(e_j+\tfrac h2(k_2)_{\rm shape}),\qquad
k_4=A_4(e_j+h(k_3)_{\rm shape}),
$$

$$
T_j=(e_j,0,0)+\frac h6(k_1+2k_2+2k_3+k_4).
$$

最后只有Pi的112行除以原port；两行均值保留且不进入下一阶段的shape反馈。$A_2$ 与 $A_3$ 各自消费，不能因geometry相同就合并。

四个局部矩阵乘法复用9c的整数dyadic kernel，所有乘加精确；/6及出口port用 Fraction。入口不通过普通float dot或longdouble得到参考。全部224个列形成一个完整 $226\times224$ 矩阵，既不删高模或均值，也不只保存三个见证列。

原local A本身的误差和真实连续流导数误差仍未认证；参考精确表示给定四个有限矩阵所定义的同一有限RK4对象。

## 一次正确舍入

rational_to_binary64_word 对每个精确元素直接输出IEEE754 word，不通过 float、Decimal、longdouble或短十进制转换。对非零有理数取绝对值并用整数比较确定二进制指数 $e$：

- normal区按 $2^{e-52}$ 的网格，以整数商与余数作 nearest/ties-even；
- 低于normal区统一按 $2^{-1074}$ 网格，处理subnormal与渐进下溢；
- 精确等距时选择偶数有效整数，必要时把有效位carry传入指数；
- 非零负数舍入到零时保留负零；精确有理零采用明确的正零约定；
- 超出finite RN范围时保存真实infinity word并报告，不截成最大有限值。

每个有限结果与精确值的差另存为完整有理误差矩阵。完整精确元素与RN原words足以逐元素独立复核舍入；结果报告ties、exact/inexact、normal/subnormal、正负零和overflow数量。若实际发生overflow，完整exact与RN文件仍保全，但不假造有限RN的作用/误差范数。

正确RN矩阵有独立原始字节SHA。它不是旧actual41矩阵，也不是新的非线性求解结果。

## 比较与完整输出

每个完整矩阵在 large-arrays/ 保存为一个文件，形状始终是 [226,224]，没有因API大小而拆成不完整子矩阵。完整有理文件是gzip JSON，schema为 complete-rational-matrix-hex-v1，含shape、order=C和226行，每行224个 reduced numerator_hex/positive denominator_hex。

| 文件 | 对象 |
|---|---|
| complete-exact-reference.json.gz | 全部精确有理RK4元素 |
| complete-reference-RN.f64le | 全部一次正确舍入的binary64原words |
| correct-RN-reference-minus-exact.json.gz | RN表示误差，全部有限时形成 |
| original41-minus-exact.json.gz | 原actual41矩阵的完整差 |
| same-call-observed-minus-exact.json.gz | 同调用浮点复现的完整差 |
| 两个candidate名加 -minus-exact.json.gz | 两个新候选各自的完整差 |
| direction-00/01/02-comparison.json.gz | 三个实际输入的完整226输出与差 |

旧/observed和候选的完整原坐标raw也保留于该目录。每个map比较均针对同一个exact参考，记录最大逐元素差的坐标与符号、精确Frobenius平方、Q/Pi/means分块平方、完整/shape/mean输出行的诱导无穷范数。另列与RN原word不同的元素数，包括符号零差异。逐元素有理差全部保留；summary不内联51k个长有理数。

对三份原输入，入口用已形成的完整矩阵作精确作用，保完整226输出，并记录参考作用与actual47原case的一致性。原shape sigma只用于224行差的诊断，均值不混入native stage行。没有误差大小阈值，没有新科学验收门；一致性标志也按实报告。

根级小文件包括：

- input-binding.json：capture、prior action、candidate、所有源及完整descriptor；
- array-manifest.json：完整矩阵/raw/误差/方向文件的SHA与形状；
- result.json.gz：完整精确统计及源/运行账；
- summary.json：小文本统计摘录；长精确分子分母留在完整结果与矩阵文件；
- failure-traceback.txt：有真实异常时保全，不把未形成对象报完成。

publisher须将整个 large-arrays/ 留在artifact，仅发布小report与manifest。不得从压缩文件大小推断矩阵维度；真实shape始终完整保留。

## 运行合同

47固定取件器已由root独立准备。候选先执行，取得其实际 result.json SHA，再运行：

~~~bash
python "$TOPIC/computations/exact_20261114_saved_stage_full_rational_reference.py" \
  --capture-directory "$VISIBLE_INPUT/native-stage43-local-j-probe" \
  --capture-result-sha256 da9715ef1685c04210d5c3d8bbfb40629fd4bf810455b497e5e25630ac0aa403 \
  --prior-exact-directory "$VISIBLE_INPUT/native-stage43-exact-action" \
  --prior-exact-result-sha256 f145cf0efea702964413abf5490df5f2ef584b373afb9b8213f001774e9ea33b \
  --candidate-directory "$VISIBLE_OUT/saved-stage-covariance" \
  --candidate-result-sha256 "$ACTUAL_CANDIDATE_RESULT_SHA" \
  --expected-candidate-source-sha256 01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548 \
  --out "$VISIBLE_OUT/saved-stage-full-reference"
~~~

若独立只生成参考，可以一起省略三个candidate参数；没有候选时明确不声称完成候选比较。正常计划是同一job先候选、后参考与比较。

参考本身只需要标准库；candidate沿已冻环境使用numpy。必须同时检出9c reader及它钉住的三个capture源码，供完整source字节校验。没有访问私有仓库、MR_TOKEN、旧完整28/41/43包或live worker的需要。

## 预算与科学边界

参考最多执行 $4RK^2$ 个标量dyadic乘积；稀疏单位输入的首stage由原kernel自动跳过零项。之后仅完整小矩阵的有理比较与三个方向作用。它不形成1372段全局系统，也不重做全部868个短J。实际耗时、每列执行乘积数、最大RSS和所有输出大小如实记录；接口不预言运行时间或压缩率。

actual47已给出：固定旧43方向时，旧new519残差平方约 $1.1148576\times10^{43}$，四A有理替换约 $6.7408926\times10^{49}$，带符号交叉项发生相消。因此当前比较要回答候选是否更忠实于明确的有限RK对象，不能把旧方向在改变矩阵后的残差当作应当改善的目标。候选形成更好也不证明真实DF、全局方程或新方向有效。完整一致系统的重解和原非线性试步留待另一次有明确来源的实际计算。

