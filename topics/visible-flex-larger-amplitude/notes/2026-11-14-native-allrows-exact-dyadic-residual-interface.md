# 原 native 完整块系统的逐行精确 dyadic residual 读回器

日期：2026-11-14。

状态：独立源码已写入，仅作 AST、原源读取与字节身份核；**尚未执行任何数值**。所有精确算术同样属于科学计算，只能在 Rogerhu12/math-research-public 自己的 GitHub Actions 执行。本组件不调用 native worker、不重算 J/RK、不解新系统、不执行 trial，也不新增原求解验收门。

源码：

    computations/exact_20261114_native_allrows_dyadic_residual.py
    36,438 bytes
    SHA256 0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f

## 1. 对象是已保存的完整有限数组

消费 actual28 原始 capture，或同一 capture 经冻结 band 源真正产生的完整原坐标方向。原布局固定为 M=112、K=224、D=576；未知方向有577个节点，每节点保留全部224个 Q/Pi 分量。原方程按以下次序排列：

$$
\begin{aligned}
e_{\rm cut,i}&=\delta_{0,Q,i}+\widehat r_{\rm cut,i},\\
e_{n,i}&=\sum_{j=0}^{K-1}\widehat J_{n,i,j}\delta_{n+1,j}
             -\delta_{n,i}+\widehat r_{n,i},
             &&0\le n<D,\\
e_{\rm far,i}&=\delta_{D,\Pi,i}-\widehat G_{D,i}\delta_{D,Q,i}
             +\widehat r_{\rm far,i}.
\end{aligned}
$$

帽号表示原捕获的 binary64 数字，逐个解释为其**精确实数值**。cut、stage n、far 分别除以实际已存的 $\sigma_0,\sigma_n,\sigma_D$。这与 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md) 的有限数组模型一致；不把已舍入的 J 宣称为精确非线性导数，也不将原捕获残差替换成另一次非线性求值。

合计129,248行，包括全部112条 cut、576×224条 stage 与112条 far。没有保留部分模式、只查最坏浮点行或把深处小量阈值归零。

## 2. 位分解与整数累加为何精确

对原 little-endian 64位字 w，令 E 为11位指数、F 为52位尾数。有限值准确写为 $m2^e$：

- E=0 时，$m=(-1)^sF,\ e=-1074$。
- 1≤E≤2046 时，$m=(-1)^s(2^{52}+F),\ e=E-1075$。
- E=2047 的原操作数无法定义有限实数组残差，明确报告相应原位、坐标和未完成状态，不用任何替代数。

每个有限 binary64 数均为 $2^{-1074}$ 的整数倍。因此任意两个输入的乘积均为 $2^{-2148}$ 的整数倍。所有乘积、线性项和残差可以在统一单位 $u=2^{-2148}$ 下计算：

$$
(m_1 2^{e_1})(m_2 2^{e_2})
 =\left(m_1m_2\,2^{e_1+e_2+2148}\right)u.
$$

移位指数始终非负。原单项 $m2^e$ 对应整数 $m2^{e+2148}$。程序只对这些 Python 整数作乘法、左移、加减，得到每一行唯一的精确整数 I，使 $e=Iu$。没有浮点点积，也没有浮点累加误差界代替精确残差。

若 $\sigma=m_\sigma2^{e_\sigma}>0$，则

$$
\frac e\sigma
 =\frac{I}{m_\sigma\,2^{e_\sigma+2148}}.
$$

同一 stage 的分母相同，先按 |I| 比较其全部224行；不同节点再用整数交叉乘比较两个正有理数。最大位置及并列选择均不使用浮点显示值。最终分子、分母按最大公因数约去，输出完整十进制整数；64位有效数字的十进制科学显示仅方便阅读，不参与判断。

原正负零位仍由原输入 SHA、见证 hex 保留；作为精确实数的零统一记为0。只有系数确为原 binary64 实零的乘积才可省略整数乘法，所有 J 位仍逐项检查并计数，不省略任何非零贡献。

## 3. 完整输入绑定与原/新方向

复用已冻结的

    geometry_20261114_native_captured_band_correction.py
    b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390

中的 CapturedArrays，保留其原 capture result/spec/summary、所有完整数组、分块顺序、原源、原 cut/尺度/far 图的验证。该模块只在 Actions 主进程内懒加载供绑定使用；其 factor/solve/main 从未调用。它的导入依赖 NumPy/SciPy，故直接沿用 offlineband 的 Actions 依赖环境即可。**本新 residual 内核与 worker 的算术只有标准库整数，不经 NumPy 浮点求和。**

钉住的原件包括：

- capture result：ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7。
- capture manifest：3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3。
- 完整 J raw bytes：394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19。
- 原完整 δ raw bytes：d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2。

绑定后新组件重新从原 raw 文件读字节并再核分块/全数组 SHA，不先转成 Python float 或另一数值表示。每个 stage 的 J 原字节也在真正消费时再次核对。

消费 band 方向时，CLI 还必须提供真实 band result 的完整 SHA。程序核其 frozen producer、same capture binding、原布局、零新增 native/J/trial 次数、array-manifest 原 SHA，并只读取其中唯一的 complete-original-coordinate-delta。不得把 band 的缩放坐标解误作恢复后的原 δ。即使 band 的后续诊断未完成，只要其真实报告已经证明完整原坐标方向已产生且全部相应文件可验证，仍可对这个已存方向作精确读回；它不会因此获得 native 接受状态。

## 4. 全行、全局最大、逐节点最大及见证

默认完成每个指定方向的全部129,248行。输出包括：

- result.json：全系统 $\max |e_i|/\sigma_i$ 的精确有理数、原行坐标与模式，全部计数、来源与完整性标志。
- per-node-maxima.json.gz：全部577个原 residual 节点的精确最大。node0 同时比较 cut 与 stage0，内部 node n 对应 stage n，末节点包含 far。
- exact-global-witness-original.json，以及请求 band 时的对应文件：全局最坏行的原 J 行、下一节点完整 δ、当前 δ、原 r、σ 等原 little-endian hex，可独立复算该行。
- exact-row-blocks：每个方向、每个 cut/stage/far 块的**所有精确残差**。每行存储规范的“带符号奇整数 hex 系数、二进制指数”；零为固定零表示。
- exact-row-block-manifest.json 与 completed-exact-blocks.jsonl：所有压缩块的 SHA、行数、kind、节点、模型绑定和规范行账 SHA。
- exact-input-model.json 与 capture-input-binding.json：完整原输入与本次方向、源的绑定。

全部排序固定为 cut→stage0…stage575→far，并列最大取原行序最早者。若同时读取两个方向，其 J 位解码共享，方向的精确累加各自独立；可直接给出两者最大范数的精确比。

此外，仅使用同一批已读的原 r/σ，顺带给出**已保存基残差**的精确范数和 $E/\|\widehat r\|_{\sigma,\infty}$。这有助使用 R266 的有限模型条件；它不是重新评估非线性残差，不能代替 R266 中单列的导数、非线性余项与浮点评估误差。

所有行都实际完成、J逐项访问数及总行数核对后，才标记 exact_complete_residual_finished=true。大的 exact residual 仍是完整诊断成功，不由本组件新增“数值必须小于某阈值”的求解门。非有限原操作数或执行中断则保留已完成分块和明确的 partial 状态，不把部分最大值当全系统上界。

## 5. 复杂度与资源建议

每个方向需要28,901,376个原 stage 乘积位置，另加112个 far 乘积。单独 original 或 band 都遍历同一完整 J；both 共享一次 J 解码，需要两个方向的相应整数乘加。

统一单位避免对每个乘积建立 Fraction 对象。完整有限 f64 的最大乘积小于 $2^{2048}$，每行只有224个乘积及两个线性项，因此本布局累加器最多4204位。这是数百字节级整数，不是随迭代无界增长的符号对象；跨节点有理比较也只在块最大值层面进行。逐行的精确值仍完整存档。

默认两个 spawn worker，允许 CLI 明确选择1至8。待处理队列不超过两倍 worker 数；每个 J stage 的原数据为401,408字节，默认最多四个这样的 stage 在队列中。主进程保存完整原/新方向和小数组的位分解，不建立完整 dense J 或另一份129248阶系统。输出逐 stage 保全，每八个 stage 更新进度；中断前的原始行账不会被覆盖。

推荐首次直接用 workers=2 完整执行，沿用 offlineband 已有环境。没有本地计时或实际性能数据，故不预先声称具体秒数。实际 report 分别记录主进程与已结束子进程的 RSS 和总时间；CPU主体是约2.89千万次有界整数乘移位/方向，而不是数千万次有理数约分。

exact-row-blocks 应整体留在 Actions artifact；Git 可保结果、全局见证、节点汇总与清单。源码不把 Git 单文件/总发布大小当作科学失败条件。

## 6. 完整执行命令

先用已钉 artifact 下载器获得 actual28 完整 capture。CAPTURE 必须指向其中真正含 result.json、capture-manifest.json 和原 raw chunk 的 native-correction-capture 目录；不能传一个仅含小报告的 Git 出版目录。

仅对原方向读取全行：

    python computations/exact_20261114_native_allrows_dyadic_residual.py \
      --capture-directory "$CAPTURE" \
      --capture-result-sha256 ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7 \
      --which original \
      --workers 2 \
      --out "$RUNNER_TEMP/actual28-original-exact-allrows"

当真实 band 完整方向已经存在后，按其实际 result SHA 同时比较：

    python computations/exact_20261114_native_allrows_dyadic_residual.py \
      --capture-directory "$CAPTURE" \
      --capture-result-sha256 ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7 \
      --which both \
      --band-directory "$ACTUAL_BAND_OUTPUT" \
      --expected-band-result-sha256 "$ACTUAL_BAND_RESULT_SHA256" \
      --workers 2 \
      --out "$RUNNER_TEMP/actual28-band-comparison-exact-allrows"

也可用 which=band 仅审计实际新方向。输出必须是独立的新目录，不得放入原 capture 或 band 输入目录。这里不提供任何未产生 band result 的假 SHA，也不以准备好的入口冒充已执行结果。

该组件的结论只回答：同一份已保存完整有限数组下，方向的真实线性缺陷是多少，普通浮点抵消读数是否反映了它。原非线性 trial、完整 native J/audit 与课题完成标准保持原状。

