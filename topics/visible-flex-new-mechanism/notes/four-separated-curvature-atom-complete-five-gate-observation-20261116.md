# 四个分离曲率原子：完整五门的64起点新观察

日期：2026-11-16。可信度：有限数值观察。64个预定起点全部返回，未找到原五门近零候选；这不证明该四原子盒无根，也不证明全部允许cap无解。主课题继续。

## 1. 本次独立的新模型

数学源为[R498](../results/R498-four-separated-curvature-atoms-and-complete-seven-parameter-cap5-design.md)，实际源为[scripts/literature_four_atom_cap5_search.py](../scripts/literature_four_atom_cap5_search.py)，参数为[request-four-atom-cap5-search.json](../computations/request-four-atom-cap5-search.json)。

四个真实曲率原子加非负远左常数，7个物理参数，始终评价原十二项密度、八个累计量、五个原门及完整物理5×7解析Jacobian。质量和间距均有R498严格正下界，真实H随形状和C变化且严格小于2。本次不是旧三原子的微小第四原子，也没有从旧 best 生成起点。

源脚本61,649 B/SHA256 1e0a0a7125ebcd77afa23ad3a297c203886d54ffdda2ae8b12b67fb29c10c5c1；request6,928 B/SHA256 455cccb65950fad0a45d699460e6f36ff9b922d280f616099fcf9e9ad838d6c9。

唯一新[run43845218578](https://github.com/Rogerhu12/math-research-public/actions/runs/43845218578)，research133223574326，report133223910029，source18a30d5054a4a2755616ca1c71fcf8870ce1f3d8。workflow为.github/workflows/visible-four-atom-cap5-search.yml。没有读取或重算旧cap15、旧36起点、旧ψ3观察或旧开发套件。

## 2. 原观察和最后时钟

原最终 outcome 为 finite_new_four_atom_model_search_no_five_gate_candidate。

- 64个固定新起点均由optimizer返回，均为其gtol终止；没有内部科学失败，也没有达到每起80次的上限。
- 新完整 value＋analytic-J：2071 started、2071 completed、0 failed；缓存命中1778。
- 原记录序号1至4272连续；正常oracle payload保留在原stdout。只读report保全部64返回、最佳原记录及完整final/clock。
- 没有原 $G_\infty\le10^{-8}$ 候选，故0次candidate minor选择、0次Decimal Newton、0次有理中心/区间收缩。
- 最后时钟 **6.541216640999892秒**，已在final report和临时文件输出之后采样，包含imports、公式准备、全部新计算与输出；无overrun。
- 原单次180秒/6000完整值账户随64起点完成闭合，不把未用余额改成后续restart。

optimizer返回只报告其自身浮点终止条件，不授原五门驻点、严格局部极小或全局最优。

## 3. 最佳未缩放原门

按所有实际已付的原 $G_\infty$ 选取的best是start46的中间oracle记录seq2925；不是把最后scaled cost最小项改称原五门最小项。

物理参数依次为 $a_1,a_2,a_3,b_1,b_2,b_3,C$：

$$
(.5633450867409526,\ .8228339423771176,\ .9071124973631786,\
 .20584912994109167,\ .4119901678434068,\ .6362893755794936,\
 .003150860674642697).
$$

其真实
$$
H=.6104871150176137,\qquad
J_{\rm sh}=.00733625434297098.
$$

原五门依次为 $\nu=1,2,3,4,6$：

$$
G=(-.0014696041957288064,\ -.0013346357018831924,\
 .0013348842641402391,\ .0010650291233758945,\
 -.0014851172678647607).
$$

故原 $G_\infty=.0014851172678647607$，远大于本次候选阈值。原scaled欧氏范数 .0011672220490143083 是另一量。该best不是已证驻点或下界；其完整8个Aj、5×7导数和chart导数仍在原seq2925。

与旧三原子的有限best相近仅是后续全图符号研究的动机。不能把两次有限搜索合并成全部cap的非存在论证，也不据此扩大或重复本次64起点。

## 4. 输出与实际pull身份

| 原对象 | 字节 | SHA256 |
|---|---:|---|
| research stdout | 13,692,982 | 9ee53e59d8e99a915b239694f4a204ce5679c0bfe1817e127223ffa34924b94b |
| FINAL_REPORT 原JSON（不含LF） | 70,523 | 61151d25ec3158d62742dc9c50a8066fb34d2c9bf74b620416b457ce5617c4a7 |
| FINAL_CLOCK 原JSON（不含LF） | 447 | 6068a52ecba2436351ae274061a01241d04498afa660cf76c3b4e9a3e3bb72a0 |
| report stdout | 317,460 | cdc6d4d62057ef7999c06f58e928f8d744531762e37f230086c8fffc193802d1 |

最佳seq2925原payload身份4c986b70833d050aceb22bd4984f52117d65b5bf78dc8e2e347fe9a1ae08ead5；最终producer chain为3a5505bbb02ac313776d935666c6ab423ba6fe10953acc366bf34a0dc46b8fa0。report复制这些producer身份，不冒称另跑科学。

research真实public pull于10:02:58.388500至10:02:58.666256 UTC读到18a30d5054a4a2755616ca1c71fcf8870ce1f3d8；report于10:03:34.618258至10:03:38.122121读到0e259e94af3666e2b110b60392dde7990d57c1a9。两次rc0，根/题README空diff，blob21bd547f56590b7f2dd279d0297efb289a9b2783与d0432faff569c8e9af7ed4809847e12880976c11未变。

对应私有实际pull读到d5a79065e80cb7ece38fd0f08576f1e536abe169及2d9aabe77e779601aebe2d8a3ac60b19dc6fda20；最后10:03:42.742401至10:03:44.026377。私有README身份未变、QUEUE本会话唯一进行中，正文不公开。下一实际pull最迟11:03:38 UTC。

## 5. 接续范围

R496仍只严格排 $H\ge2$，完整待解范围 $3/5<H<2$ 未被本次数值排除。继续处理完整凹图和原式联立符号条件；不靠追加相同起点收尾。并行主几何已到真正接受56，其非零新场全168联合模型正在实现；这些局部门和数值接受都不替代主完成标准。
