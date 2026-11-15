# R786：原五次幂基的准确短展开已完成

2026-11-15，serre-public-astra-20261115。本文登记公开仓库自己的
[run 43682100611](https://github.com/Rogerhu12/math-research-public/actions/runs/43682100611)
的实际结果；[R786 理论证明](R786-original-power5-sections-and-129-Laurent-recovery.md)
及原映射、原相位不变。

## 1. 实际结论

该 run 已成功生成原 $V_5=H^0(Y,5\mathcal L)$ 的全部 1234 条基，
每条保留 $q_Y^0$ 至 $q_Y^{128}$ 的全部 40 个 $\xi_{41}$ 坐标。
基的次序、乘积配方与 R775 已完成的 power5 阶段逐条相同；
统一整数尺度为 $82^{10}=13744803133596058624$。
全部短展开都与原 R775 的模 739 系列准确比较通过。
原已证非零 minor 的行数及列数均为 1234，模 739 行列式为 514。

这里第一次生成的是上述原基的特征零短展开，没有重复原基选择、
拓扑、周期、整数格或 R774 的 $H^3$。
R775 原生产者虽然因预算返回 exit 124，但本次只使用其中六个
`complete:true` 文件：M2、power2、power3、power4、power5、determinant cosets；
不使用未完 power6，也不假定原 R775 全任务成功。
这些文件的真实 run/source/ZIP/manifest/逐文件 SHA 均由请求及 wrapper 核对。

这不声称已经求出 $L$ 上关系核、原 $y$ 映射、$\beta$ 或高度。
后继使用 R781 已完成的 $R_0,\ldots,R_{128}$ 及 $\kappa^{129}$，
依 R786 的全部 129 个 Laurent 条件求解并准确代回。
理论 Schur 尺寸 $1326\times1214$ 与秩上界 1186 不当作实际计算秩。

## 2. 完整复现绑定

源提交：`dd262672a8b1e2af82277b15e0fa766038609670`。
执行环境：本公开仓库 GitHub Actions，Python 3.12、python-flint 0.9.0。
算术 core：`scripts/R786_exact_power5_short_basis.py`，SHA256
`4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851`。
理论证明 SHA256：
`c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d`。
全部参数、生产者和原尺度见
`notes/R786-public-exact-power5-short-basis-request.json`。

输出绑定如下；SHA 均为 SHA256。

| 对象 | 字节数或数量 | SHA |
|---|---:|---|
| 临时 ZIP，artifact 14148389754 | 111049026 B | `52caf389aeeebd7e3d21006fc235b03fd350afe4f5e2065120a1ad86c98d71c3` |
| `full-outputs-manifest.json` | 1085673 B；3740 文件 | `e3c29e85236c8cc665bdf88e9ffd2bbab9180b6f977f0b2b22f54266762f405a` |
| `p41-exact-original-power5-short-basis-certificate.json` | 完成证书 | `dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9` |
| `R786-exact-power5-basis-index.json.gz` | 70056 B；1234 基 | `0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35` |
| `R786-exact-stages-manifest.json.gz` | 185110 B；3733 stage | `f8bf6c1d9968b0acd3664b2480efbe9d6563a0a61ef4bd027fff3bf96a4d3f02` |

小回执位于 `computations/R786-exact-original-power5-short-basis/43682100611-1/`。
其 run 回执为 `complete:true`、exit 0，core 回执显式标记
`actual_y_map_claimed:false`。公开 job 132714728448 的计算、临时转交、
小回执发布和最终证书检查全部成功。

root 复核了 core/wrapper/原阶段格式、Actions job 与回执，
并下载实际 ZIP 核其 SHA、manifest SHA，以及全部 3740 项的字节数和 SHA。
这只是文件完整性检查，没有本地重算数学。
可重算展开和证书不入 Git 或 Release；活跃断点仅以一日临时 artifact
转交直接后继，2026-11-16 05:41:45 UTC 到期，消费后清理。

主目标仍 OPEN。原 p41 分类 R707 已关闭，本任务服务真实函数与高度输入，
不重新执行该分类，也不将这一固定素数的结果推广为一致性证明。
