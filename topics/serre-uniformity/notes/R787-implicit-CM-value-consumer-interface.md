# 原 518 current 的 CM 收缩：首次执行接口

本接口消费已经完成的原方向，不再提升该方向，不重建原 Schur 块。
数学依据为
[原单位选行块与点值证明](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)，
SHA256 `8d5b58a5f6e9748805af3c032de1bae955543b1855535b6c51f0ca9cd6947820`。

核心为 `scripts/R787_implicit_CM_value.py`，结果类型
`R787-original-implicit-CM-value`，最终文件为
`p41-original-implicit-CM-value-certificate.json`。
CLI 是 `--config --proof --retained --output --budget-minutes`。
核心仅使用标准库的准确有理数和原十四维首一商环；它不导入旧数学核心。

## 一、实际来源与最小载体

来源全部通过原 manifest 的 bytes/SHA 和原 run/core/input 链绑定。
包装器只导入已冻结的标准库 Range IO helper；不导入数学核心。

| 原来源 | 本次携带的完成输入 |
|---|---|
| R787，run43737413555，原93d3核心 | 518 current、原 chart/selection/rational-blocks、四个 metadata 文件，共8件 |
| R790，run43688215703 | 原146个 P1 值/首jet、cert/stage manifest、metadata，共152件 |
| R775，run43679160495 | 原 M2 与 power2–5 recipes、cert、metadata，共10件；由 R790 已保载体运输 |
| R786，run43682100611 | 原 power5 cert/index 与 metadata，共6件 |

输入总计176件，旧字节不改。新载体
`R787-implicit-CM-retained-inputs.tar.gz` 只装这四组所需输入；续算直接恢复它。
R790 的旧载体只在首次运输时用于恢复 R775，不在新载体内再嵌套一份。

原1234条 q 展开和 R781 的 Laurent/R/κ 文件不参加本次数值收缩。
原 R787 manifest、原 R786 index 和旧配置中的 R781 完成来源仍准确绑定其身份；
输出表达式列出原 F 文件的逐项 SHA 及 R781 来源。
未来若执行准确行列式或行空间零认证，须从仍活跃的原载体读取这些实际原行，
不能把本次未展开的矩阵表达式说成已物化的大矩阵。

历史来源 README 的 SHA 与当前执行 README 分开核验。
工作流首先真正 partial/sparse checkout、`git pull --rebase origin main`，
只在根/本课题两 README 与已经读过的规则相同后执行数学。

## 二、唯一的新算术路径

1. 从1234条原五次 recipes 反向取依赖闭包，只合成实际需要的 power2–5 节点。
   原 R790 的 $a+b\zeta$ 准确转换成 $(a-b/2)+(b/2)s$，$s^2=-3$。
   值和一阶导用双数乘法；已有 $82^2$ 尺度保留，五次不再额外乘 $82^{10}$。
2. 用原准确整数 $Z$ 形成 $e_0Z,e_1Z$。
   `Z_pivot_integer_rows` 已包含负号，本次直接加它，不再取负。
   此路径不另行展开当前 $ZC$ 分母向量。
3. 用旧518 current 形成 $A_0,A_1,B_0,B_1$ 四个十四坐标模响应。
   全部计算留在原 $B_{\rm fld}=\lambda b,s$ 基中，不再插入共同分母、content 或 $\lambda^i$。
4. 在原14个模 $\ell$ 分支评价 $B_0$。
   任一非零分支给准确特征零非零见证；全14个单位才允许整体十四维商环求逆。
   初始逆直接使用旧 selection 已存的评价逆矩阵，之后只做标量 Newton 倍精度和完整十四坐标乘回。
5. 若全环可逆，保存 $y_0$、$y'_0$ 的518位模坐标。
   对每坐标仅尝试一次严格有理重构，并把结果保存为候选。

各准确 product/eZ 与模 contraction 按32行/列原子完成。
完整块始终同新 source/tag；预算耗尽保留所有已成块。
标量环逆也在每个完成精度保存，可直接续到518而不重复完成步。

## 三、表达式、模值与准确坐标的边界

最终证书明确分开：

- `exact_implicit_relation_defined=true`：由证明 U.1 的2420阶原选行块定义原准确关系；
- `exact_finite_y_implicit_expression_defined`：仅在实际非零分支证明 $B_0\ne0$ 后为 true；
- `modular_value_computed`：仅在14分支都是单位后为 true；
- **`expanded_coordinates_exactly_certified=false`：本次始终为 false。**

表达式保存 $M=[F_A,-C_{P_S}]$ 的原选行、负号、free1186与原数据来源，
四个准确线性响应，以及
$\Delta(\ell,c)=\det\begin{psmallmatrix}M&r\\-\ell&c\end{psmallmatrix}$。
它不声称已经求出准确大逆或展开过行列式。

有理重构建议即使14坐标全部得到，也不会变成旧 R792 的成功 recipe。
本次没有执行原 $L$ 中的 bordered determinant 零认证或准确行空间乘回，
不会填原 $x_0$、不会宣称完整 $\beta$、η 或高度已算。
若模 $B_0$ 在某些分支为零，仅记录实际分支状态；不由此宣称特征零共同零或点为 $O$。

## 四、输出与续接

所有新阶段为 `R787-implicit-CM-*.json.gz`，各自带新核心 SHA 与固定数学 tag。
原当前518、原四组来源身份、证明 SHA、块长32、固定 RR 算法全部进入 tag；预算不进入。
最终 stage inventory 用内容命名，列全部完成阶段；预算中断没有伪造最终证书。

包装器以 budget×60+900 秒设置外层终止，先 TERM、短宽限后 KILL，
照实保缺失 core receipt 或未完成状态。恢复只接受同核心/同 tag 的完整旧阶段。
最终验证遍历实际输出 manifest、输入载体每个成员与所有阶段来源引用。

源码、参数、本文及简明运行/SHA登记可入 Git。
准确值表、模响应、表达式数据、机器回执与可重算候选只随一日 active artifact/carrier 续传。
