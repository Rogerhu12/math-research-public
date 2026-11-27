# R1121：原 full47 六个 CM 盘的十二条第三类微分值

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，新的公开精确计算全部成功。**
在原 $X_{\rm ns}^+(47)$、辅助素数 $q=4513$、同一原 Hodge 帧及
$z=j-j_{\rm CM}$ 参数上，下面六个原 CM 点的
$Z_A=13R_0+4R_2$、$Z_B=2R_4-7R_0$
两条规范第三类微分值均已准确读出。
几何、完整除子、粗模尺度、全部 cusp 及 Cartier 归一采用
[R1118](R1118-original-short-Cartier-reading-for-CM-third-kind-values.md)；
原 QC 接口采用 [R1103](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)。

本次只计算这十二个尚未完成的 case。
标签0、141的四条有限 Miller 请求仍独立在途；
不会把本次某条除子在其它目标处的导数当成那四条缺失的值。
QC 实际行秩另由已审消费者计算，本篇不提前宣称盘内唯一。

## 1. 实际执行

- source：[1340d243733c1693ac57aa04043b7b9194fd14ed](https://github.com/Rogerhu12/math-research-public/commit/1340d243733c1693ac57aa04043b7b9194fd14ed)。
- [run45994669183](https://github.com/Rogerhu12/math-research-public/actions/runs/45994669183)，
  [job140490956495](https://github.com/Rogerhu12/math-research-public/actions/runs/45994669183/job/140490956495)，attempt1。
  checkout、固定镜像、数学步骤及整个 job 全部 success。
- 数学总耗时 **541.158560016秒**；预算18000秒、reserve120，
  四个工作进程，共用完整截止时间。
- 固定 SageMath10.6 官方镜像，python-flint0.9.0 的有限域源与 Sage
  使用 fresh-exec 隔离；无本地数学执行。
- 完整 receipt 的 status=complete，completed恰有12条，
  failed_cases为空。root/global分别读取完整公开 job log；
  root另核全部清洁行和共同证书的 canonical SHA-256。

## 2. 十二个实际值及尺度

全部值均属于 $\mathbf F_{4513}$，已经除去清分母的6：
$$
\alpha_{Z,y}=
 \left.\frac{1}{6}\frac{\eta^{\rm fix}_{6D_{Z,y}}}{dz}\right|_y
 =\left.\frac1N\frac{d\log\bar f_{D_{Z,y}}}{dz}\right|_y.
$$
这里第二式只说明与 R1103 同一规范值的数学身份；
本次没有执行或冒称执行有限 Miller 的整数倍链。

| 原候选标签 | 原 CM 判别式 | $\alpha_{Z_A,y}$ | $\alpha_{Z_B,y}$ |
|---:|---:|---:|---:|
| 76 | $-7$ | 2478 | 1979 |
| 77 | $-27$ | 2484 | 4348 |
| 100 | $-28$ | 4045 | 3940 |
| 108 | $-8$ | 1449 | 1184 |
| 196 | $-16$ | 689 | 593 |
| 220 | $-12$ | 2875 | 295 |

每条记录同时输出该**同一除子**在全部八个原 CM 点上的规范微分值，
顺序为 $[0,76,77,100,108,141,196,220]$。
其中本表的 $\alpha$ 严格取本 case 自己的候选标签位置，
不会在八点之间交换除子。
每行保 method=R1118-short-Cartier、coarse_parameter=j-j_CM、
clearing_denominator=6、order_mod_q=551，
以及实际除子、完整 RR 来源和规范修正的哈希。

## 3. 有限 RR 的完整成功证书

两类实际清分母除子仍是 R1118 的完整 $6D_A,6D_B$。
没有删掉 cusp 项，也没有把扩域支撑点缩成单个代表。

| 对应 | 约化支撑度 $s$ | $\dim W_S$ | 分子空间维数 | 留数矩阵秩 |
|---|---:|---:|---:|---:|
| $Z_A$ | 159 | 103 | 231 | 158 |
| $Z_B$ | 151 | 111 | 223 | 150 |

这分别准确等于 $262-s,\ 72+s,\ s-1$。
每个 case 都证实 all_original_cusps_included=true。
分母截面按 R1118 的确定性线性避让选取，完整条件逐一核验；
full colon 达到已证维数后才结束，不以一个任意双截面近似完整条件。
标签77/$Z_A$ 在一条 colon 约束后即达准确维数；
其它十一例使用两条。全部仍核完整支撑、全部留数和目标等式。

## 4. 同一原帧上的完整 Cartier 算子

除去本次支撑中的 Gaussian 点后，共保留432个实际自由标记；
选择其中73点时取得
$$
\det E=3058\ne0,\qquad k(0)=809,
$$
物理参数准确为 $B$。
相应的73个原 Hodge 值列和73个 Cartier 值列均完整计算，
并在原基上恢复 $C_{\rm col}=E^{-1}E_C$。

实际原整格检验为
$$
\boxed{\det(1-C_{\rm col})=551\ne0.}
$$
因此每条规定留数微分的修正
$$
x=(1-C_{\rm col})^{-1}(C\eta-\eta),\qquad
\eta^{\rm fix}=\eta+\sum_i x_i\omega_i
$$
唯一，并准确读取原 Cartier-fixed 规范值。
列作用与原 Hecke 的 row 作用之间保留转置：

| 证书对象 | SHA-256 |
|---|---|
| 完整 Cartier column matrix | 21fc43c13f58e974adb58804e3480f80d3268104546e31e40ca5370806bbb58f |
| 完整 Cartier row matrix | deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d |
| 全73帧的完整计算值 | 31af31bc4fb3a6eaa458c90397203fee74529ee4e29b2319267bde60c2d030e8 |
| 原 Hodge 评价矩阵 | 8c5073af02da9d9731f7cbff7ab5fa1e061e590fe965355c9a2e79ff463795bb |
| 选定原帧 | ac2b0b2dc168977fe758cbf9b6f9a2eeb5b187d6da566f0940f824c9f375c67f |

这里没有用特征多项式一致替换原坐标矩阵一致。
后继 QC v2 还将把 R1120 的 $1-B_q(H)$
与本证书的原 row matrix SHA 作完整交叉核验。

唯一一次必要的4513阶 Gaussian 格点再生核对旧完整 grid SHA：
627e076ae64de06332324f1bdf0a82e2888b493f4799af3b7211c6d7524d7c50。
共2208个非零47挠标记，Weil根仍为2。
没有重算旧 CM 高矩或另登记旧对数值。

## 5. 完整请求和结果哈希

| 对象 | SHA-256 |
|---|---|
| 新 short-Cartier consumer | f78bbb0e701de91afe2af5a7189948bc92055d62a6c2bfad13343af08e4e2adf |
| 新 closed-support consumer | 6e2221fa6e3fb8b5624ec76ee5fca36ef211cacc288708700c84c32d046f6b59 |
| 本次方法说明 | a7cfec96ed279a1824ed3faa614c034e53845f584aa5e0f381283fb91829ff09 |
| 实际请求 | 20db24c6c8857df91109713833b47fcd2db5fd0930e45b4703f7017befb49f84 |
| 十二条完整清洁结果行，按id排序 | 895d06ff05fab216225b5a6794295b3fb731d4ea5d1982935db365a4ebddcc09 |
| 完整共同 Cartier 证书 | 3563933eb15259bdcaddb70d97b6b56c869e8fe3c997b0d64e16030caa7d9bfb |

入口为
[方法](../notes/2026-11-27-full-p47-short-Cartier-third-kind-method.md)、
[请求](../notes/full-p47-short-Cartier-third-kind-request.json)、
[主程序](../scripts/full_p47_short_Cartier_third_kind.py)、
[实际支撑程序](../scripts/full_p47_Cartier_support.py)。

完整矩阵、73帧级数及中间 RR 数组只在 runner 内存或临时目录中，
没有提交 raw、artifact 或 Release。
后继请求仅消费上述完整小记录和证书；
不重新计算这十二个已成功的值。

## 6. 当前后继

R1120 的四基本 CM 全 Hecke 坐标及本篇十二条实际局部值已同时齐备。
因此现在为这六个盘提交完整 QC v2 首行读取，
保原73维 trace、全部高度、原 $B_q$、固定角和实际切向尺度，
再读取真正的 $t(B+At)$、共同 gcd 与单位导数。

若首行不满足唯一性判据，将继续其它对应或更高层；
本篇只登记已成功的输入，不预写下一次执行的结果。
即使固定47全部关闭，课题 README 的绝对 Serre 一致性主目标仍须继续。
