# G10第二源失败：连续arc累计审计修复，独立target g保持

## 1. 真实失败，没有dense基线或步数

G10r的192角observer源在外部1302.392905433秒后自然exit=1，peak child RSS251164KiB。原外层polar逆图在新增源行502（s=.5700611962786817、角157）出现残差1.4921397450962104e−13/括宽8.88e−16；内层收紧2e−15后已得到过外层5e−14门的返回根，但后续高精primitive审计失败于残差2.632442874794805e−16。

逐行完成journal明确最后completed=502，对应最后已保存s=.5689705599985317。只有前502行获正式完成回执，剩251行重做。原门控driver检查真实source exit1后抛RuntimeError退出，**没有产生G10 prepared、baseline或接受**，未将缺失source误当成功。

## 2. 数学arc与旧binary64锚分开

原Curve入口明言：数学弧长由积分定义，有限quadrature/cumulative只是数值求值。上一版高精审计保留binary64累计锚，却高精重算各panel局部primitive；两者在panel界可能差数个ulp。此时一个以旧锚选定的panel内确实可能没有精确根，继续把局部残差硬压到8e−18没有数学依据。

新独立helper `2ecf-polar-refined-arc-source-evaluator.py` 在reference审计内以同一冻结Fourier系数重算：

    L(t) = integral_0^t |gamma'(x)| dx,
    raw.a = L(2*pi)/(2*pi),
    normalization = fixed_exact_target_radius/raw.a.

用longdouble的完整一致period/cuts，从0计算每个panel积分并累计；分别做Gauss16与Gauss32。物理fixed_exact_target_radius=1.005432838021469保持原字面值。重新计算的raw.a及normalization是同一积分定义的数值近似，不是另选自由目标参数。

**独立target metric a0完全不由这次reference重积分产生。** 恢复source输出仍使用原literal source、原半径参数和内层2e−15求值；新primitive只在这些实际返回根处核角方程及端profile，不写回生产source/target。审计前后对原目标oracle再取该s的a0/a0_s/a0_ss，确认完整字节不变。

## 3. 原失败点的实际数值

| reference量 | Gauss16 | Gauss32 |
|---|---:|---:|
| 新raw.a（longdouble） | 1.0054328380214688363 | 1.005432838021468819 |
| 与原raw.a数值差 | −1.5233040523e−16 | −1.6967763999e−16 |
| 新normalization−原1 | 1.5146304350e−16 | 1.6881027826e−16 |
| 最大旧累计锚前向差 | 2.1471539824e−15 | 2.0805839690e−15 |
| 新primitive实际逆图残差 | 4.3368086899e−19 | 4.3368086899e−19 |
| 固定返回根处最大角残差 | 7.6516484121e−15 | 7.6514315717e−15 |

ref period为6.283185307179586477，与原binary64 period差2.4502969098e−16，记录未隐藏。原实际tight-source返回根的自身外层残差6.2172489379e−15；独立重积分reference仍远低于原5e−14外层门。相同根处完整polar profile两jet最大差：rho<=1.3803e−12、logrho<=1.2861e−12、z<=6.3783e−14。

实际audit进程自然exit=0，22.948857972秒，RSS149304KiB，目标oracleexit0。原8e−18内审门、原5e−14外层门均不必放宽。以上是有限高精数值审计与显式前向差，**不是严格积分区间证书或全域source误差上界**。

## 4. 独立G10s source消费者

旧G10r和G11r所有入口/SHA保持不动。新 `2ecf-polar-c2-g10-split-prepare.py`：

- 逐字采纳已完整自然0的958×128 training组及其所有来源回执。
- observer仅恢复逐行回执证明的502新源行，实际重采索引0/251/501核六jet及target radius字节。
- 剩余251行拆成不相交[502,610)与[610,753)，各有独立真实source进程和自然exit0门，分别108和143行。
- 两chunk、旧完整training、旧205源行及正式observer前缀完整验证后，才合并新958×192组、assemble新prepared。partial失败和新source进程的成本分列。
- 原数学source、独立g、完整12789列、128/192角和每span完整G10均保持；新数值consumer和其一致arc审计另有明确SHA。

本条审计形成时chunk正在实际生成；完整新prepared和G10新baseline/真步需自然成功后分别登记。已启动新的门控driver，不使用已失败旧driver留下的任何不存在结果。

## 5. 身份

| 文件 | SHA256 |
|---|---|
| `polar-c2-G10r-observer-source-exit.json` | `f544224d6a2a69cd807aa57a6ad70effaa42588a498ce1fbf37cc3d6f2810401` |
| `polar-c2-G10r-observer-source.log` | `0e5e8737ba37a0869a347f031b67fe636ecca914e40df6add769d06e7418fe03` |
| `polar-c2-G10r-observer-new-completed-rows.jsonl` | `f2dd3d6478d9b9d81b6a65b21759209e321887ee3a15ac83358a014273055504` |
| `polar-G10-actual-first-step-driver.log` | `365a3e55c988deefa1016374186d0eb037679f513f3bc83788bf7003d8085c96` |
| `2ecf-polar-refined-arc-source-evaluator.py` | `fa33a49b999b5266da9faffc6f4eb8fece36539f71d10f6a8ee39ba0ba893f5b` |
| `2ecf-polar-G10-consistent-arc-audit.py` | `ad3fa480024463e6ffb0660bca428d91b5709ab1764ee46e5bb3d1b4349f2d55` |
| `polar-G10-consistent-arc-audit.json` | `ff817ef9d36dc616206512b368503fbb84ab86ce14b16681f15ec2b1105491ec` |
| `polar-G10-consistent-arc-audit-exit.json` | `aa5b97ba4e4837c59459f3d14a9ddb62ff09c17b0c6279a8d46b1e7df064a613` |
| `2ecf-polar-c2-g10-split-prepare.py` | `fe7946d5b0156dcc507ee10bb387080179af5269ceb004e6c7630ff80279e04b` |
| `2ecf-polar-G10-split-actual-first-step-driver.py` | `8fac52c2b4caff42255cef3d9ad9bb5a32149101512b27732eaf6afdeddd214f` |

没有原目标收敛、连续reach或课题完成宣称；原固定g实步与独立新g设计继续。

执行源码的 `longdouble_primitive` 历史docstring仍有“旧anchors/normalization冻结”字样；该字样不描述此版本实际reference。实际实现及receipt明确从0重新积分累计并按固定物理半径重算reference normalization；原生产source输出和独立target g保持。为保已执行源码SHA，活动消费者不就地改文案。
