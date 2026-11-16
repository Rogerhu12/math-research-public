# 完整 cap5 单次积分证书 LP：达到 solver 限额而无候选

日期：2026-11-16。**实际已完成并闭账；没有得到有理证书，没有证明有限 LP 不可行，也没有判定真实 cap 类有解或无解。** 继续完整同图五门问题，不重启本有限实例或旧原子搜索。

## 1. 唯一实际来源

| 项目 | 原记录 |
|---|---|
| 公开 run | [43859053666](https://github.com/Rogerhu12/math-research-public/actions/runs/43859053666) |
| research job | 133270754815，completed/success |
| 只读 report job | 133272518079，completed/success |
| source commit | 4e8575cdc0610ca185979938d88e2485201869d3 |
| workflow | .github/workflows/visible-complete-cap5-integral-certificate.yml |
| request | request-complete-cap5-integral-certificate.json，10263字节 |
| request SHA256 | 27f9e118eece47cbf30426efab32feb1a3517975084918e6cc2ea6f7a2be4756 |
| 原 research stdout | 117573字节；SHA256 bf1f2bc1f570ef774926d5369f8e032b5f3b73c8ce19087762797e9344ac0c87 |
| 原 report stdout | 133597字节；SHA256 ada435c937b0a17a80636811e966c56118411413edee2262502115459c002c33 |

冻结数学与源码见[完整设计](complete-cap5-integral-positive-certificate-design-20261116.md)及[唯一新范围](complete-cap5-integral-certificate-single-new-scope-20261116.md)。完整原十二密度、八累计量、五门、C尾、85端势、九真不等式及固定参数/空间次数均按请求使用。数学输入身份为e913603c97c3ccbe59e2351e552f1d34d0c111160f8ef51881c5e051afb3c295。

## 2. 实际组装和唯一 LP 返回

实际不是静态上界：组装完成20,525变量、31,809行、672,136个非零entries，合并后仍672,136。变量由40个n正负部分、1530个B系数、18954个非负乘子和1个epsilon组成。全部20,525列实际开始且完成。

| 实际阶段 | 原耗时（秒） |
|---|---:|
| 完整原五门系数组装 | 0.013183987000005004 |
| 固定新LP组装 | 2.912308201000002 |
| 数值依赖导入 | 0.6562625809999929 |
| 稀疏LP构成 | 0.011852701999998771 |
| 唯一HiGHS调用 | 180.12341832500005 |

所有阶段都属于一个总钟，不能在最终费用之上再次相加。

唯一 solver 请求180秒，返回status=1、success=false，消息为 time limit reached，primal_status=None；nit=270738、crossover_nit=0。原x为None，候选维数和目标值均为null。保完整返回，没有用零向量、最后猜值或缺失数组替换。

由于没有候选，有理化/精确judge开始与完成计数都为0。因此本次没有任何 $E_{\min}$、$D_A$、$D_Q$ 或严格余量的实际计算结果。不能把未运行的精确判准写成已失败、已通过或已检验的零。

## 3. 原最终费用与输出身份

权威最后 CAP5_CERT_FINAL_CLOCK 在完整报告写入和stdout flush之后取样：

- 总科学费用 **183.90384485000004秒**；
- 固定总限额600秒，overrun_after_nonpreemptible_output=false；
- 新LP started/returned=1/1，exact judge=0/0；
- 新旧cap求值、旧mapper、旧rank、development tests 全为0；
- peak RSS244436 KiB；
- 12个完整科学records，单调且连续，原记录字节9507；
- 最后record chain为7536c58e740add6b1dd30a2b247d463fedef6553c22c0cfa724f58857f1efb58。

本账户随唯一LP返回闭合。600秒总钟是上限，并不授权违反原“一次LP”约定再启动第二次；未使用余额不迁入重启或改变次数/区间的任务。阶段返回后不重新执行科学检查。

| 原语义记录 | JSON UTF8字节 | JSON SHA256（无末LF） |
|---|---:|---|
| LP_return | 659 | 570e9773cb6e2cefaf1cc04eecc4a91e165da8705fefb27f7aeafa8e9057e0b9 |
| FINAL_REPORT | 4378 | 386cf4e1849f0a7b43456ed225e59289f6289916c2641dbaec289ce8eb3f4608 |
| FINAL_CLOCK | 808 | 004d3517ffe24d3bfdf201598ef63f3425d993ffdbee7af39cd73d8049fe903a |

LP_return payload SHA为85bfe81c2505c5aeb6b193f262e0326a2f93c5ecedcfdf480b576dfcb61d9c37；这是payload身份，不混用其外层record JSON身份。

只读observer完整读取一次原研究log，14个保留记录含12records与两个final，0parse errors，序号连续，无投影限额或结果缺失。observer_seconds=1.6819919120000009，单列为读取费用，不加进科学总钟。observer成功与research退出0表示输出任务按计划结束，不表示证书成立。

## 4. 每次真实 pull 的规则记录

| 阶段 | 真实pull完成（UTC） | 已读上游commit |
|---|---|---|
| research public | 11:35:38.614649 | 4e8575cdc0610ca185979938d88e2485201869d3 |
| research private | 11:35:41.315963 | c52bd670a315dae69326d355e326e4a088e55222 |
| report public | 11:39:09.366785 | 55f9e1f52f3a2b126a8cb1aa082424467a2cc732 |
| report private | 11:39:13.878801 | fcdd4b406abefbb3b3942b74dace7444017aa3ec |

每次公开根和本题README都空diff，根blob21bd547f56590b7f2dd279d0297efb289a9b2783、题blobd0432faff569c8e9af7ed4809847e12880976c11未变。私有根blob5ba164843b1f5802184178a82d786264404873a3未变，题README不存在，QUEUE本会话唯一进行中。私有正文未输出，MR_TOKEN在科学/observer入口前移除。

## 5. 这一结果的准确边界和继续项

原五门及全真实cap类仍未判；本次连有限LP的最优值或不可行性也未判。R499高度窗与R502同图offset多项式的纸面结论不因这次有限超时扩大或失效。

继续真实Re/Im同图耦合、可给解析严格分离的完整组合，或新的真实共同零构造。只有数学问题或具体结构得到新推进时才设新的必要科学任务；不把相同有限instance重跑算作新研究。57全168非线性任务与同母规范路径理论并行推进，主README完成门仍未满足。

