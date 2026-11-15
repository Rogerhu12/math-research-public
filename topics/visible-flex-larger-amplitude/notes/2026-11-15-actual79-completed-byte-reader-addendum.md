# Actual79：完整字节读回附记

类型：既有科学结果的原件字节完整性附记。  
作者：ChatGPT / amplitude。日期：2026-11-15 UTC。

## 结论与来源

第79轮原完整 artifact 已由独立只读 Actions 完成导出字节核验。本附记将五份原报告副本、此前精准取得的四份相同报告、实际新 warm、62源 primary 身份回执和17项父/报告关系对应。原接受1/32、最近拒绝left-RMS465、FD通过和BVP未接受范围均一致；没有重跑科学，没有新增接受门。

原科学 run 为[43663293492](https://github.com/Rogerhu12/math-research-public/actions/runs/43663293492)，source `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b`。原 artifact14141611284为639331603 B，ZIP SHA `c2432e485c0d7e1c2a047d43ade9b0ec9bb159a1e266c8cee81a1b163f298257`。只读 run 为[43665645276](https://github.com/Rogerhu12/math-research-public/actions/runs/43665645276)，source `084d2a293d0709eace0d39aa871cd68fec9e3a23`，job132664288912，全部success。

root唯一下载本次956856 B小 artifact14141838540并核size/SHA/CRC；本地marker与 `968f8a366d00548348de6ce0a1bc31be2226dfa6db031354c3b7effbe78ecf9a`一致。本次本地没有再下载639331603 B原科学ZIP。

原读者为冻结24-query reader `1aa4da4e721aa12a9f4d6257e3a6b6a7b328059de217ba42268d73a018e9828c`。主摘要63708 B，SHA `e3878efd3575a7e153769a9052567299468073b9a7b98d67a634663bdfca25cc`；完整Actions审计805949 B，SHA `062b388c549687b72eaea6cd7e53617220cc5117550c4ebf7286c824ca25bc3c`。

本地只执行标准库JSON解析、流式SHA、原字节比较与整数布局核对。完整逐项对应见[附记回执](actual79-completed-reader-addendum.json)；原完整Actions审计另以[无损gzip副本](2026-11-15-actual79-complete-original-byte-audit.json.gz)保存，解压后为上述805949 B原字节，未重新序列化JSON。该gzip为94111 B，SHA `4dd8e1588b88c07ca9ed998fc4ec818ea3504ca891ccfab9c585f3152814e519`。

## 24组原查询与完整支持

本轮是从actual76保存warm沿同一冻结24-query类重新形成一次模型，未在第79轮新增query。16组left-RMS与8组原collocation midpoint各2048角，共49152行；left依次为466、467、468、469、470、471、472、473、475、477、479、480、481、482、484、485，midpoint依次为473、475、477、480、481、482、484、485。

声明维数与实际B列并集均为7101，即466–486的21份338维物理节点及3个全局control；`zero_layout_nodes=[]`，零布局列数0。24组679列映射逐项对应原完整索引。reader中的 `added_original_left_RMS485=true` 是24-query类相对其23-query前身的来源历史，不能误写成第79轮又添加一次485。left485和mid485始终分开。

实际本轮B model SHA为 `656a644d77d438deb67f454a8c588ae9c05043570691072d6779300c92157fc3`。原88次Jacobian调用中仅捕获59、61两批，保存21个唯一端点/21份版本。原C修正仍为4059维；完整outside offset、完整B和完整H恢复保持各自范围。本附记没有重新构造A、B或H。

## 完整Actions读回范围

| 原件范围 | 实际核验数量 |
|---|---:|
| domain NPZ / 内含NPY | 215 / 1396 |
| 全B、Gamma、Pi拼接 / 全typed beta拼接 | 72 / 1 |
| condensed NPZ / 数组引用 / 唯一完整数组 | 108 / 42 / 38 |
| 凝聚与恢复raw文件 | 14 / 415120992 B |
| 完整读者实际源码SHA | 71，缺失声明0 |
| collocation observer原报告 | 17 |
| midpoint observer原载荷 | 6，全部有原descriptor |

domain覆盖所有B/Gamma/Pi分块和拼接、beta、mesh、原state/RHS、尺度、中点和捕获端点J/P。condensed的完整组成部分与引用均保留，无basis截断。14raw覆盖原g、局部索引、原仿射及其误差、7101维局部平方根/仿射/梯度/中心，以及原恢复向量、右端、局部不匹配和原H残差。

observer记17次原evaluate、1次原weights、0次observer错误，无额外RHS/J/model/trial。原Actions实现检查值为adjoint error `5.41044007575205e-18`、local/full error `0.0`、完整complex-chain relative error `9.904960962078049e-13`。这里只读取原值，不重新计算这些误差。

原primary回执的17项父/报告关系全部为true，其62份源码SHA逐项是本次71源清单的同名子集。额外9项均为历次observer源的完整覆盖，名称原样保存在附记回执中；不将62和71混称同一审计范围。

**完整链QR因子仍只保留于原进程内存，没有导出完整因子文件。** 已核局部平方根与14raw不等于独立完整QR因子审计，也不是再次验证整个A/H的数值实现；原对应false标志未改。

## 原科学结论和父子身份不变

status、model、comparison、QP summary、FD五份原副本全部长度/SHA与descriptor一致。status、model、QP、FD四件与此前公开取件逐字相同；新warm压缩字节另核。主摘要的accepted/nearest字段逐层对应原trial，对缺失可选字段补的null单独记账，不当成新原值。

真实父仍为actual76 warm `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f`、原status `a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5`。新warm为 `565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504`，新status原解码SHA为 `e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0`。完整父producer子树保持。

全部6个原试步已保留。原接受1/32，两组完整RMS域通过；本模型固定W下merit从43.57627837509625降至43.5661119869748，原drop为0.010166388121447767。最近1/16的所有节点/中点及24组已建模角有效，merit下降，原全RMS仅left-RMS465失域，beta²为−0.421944063367393、phi为0。较远1/2的mid487失域不能冒最近限制；下一只补left465的既定决定没有因本附记改变。

原完整affine FD四阶相对误差仍为 `1.006440735979892e-9`，绑定真实新warm/完整producer；它使用真正零H T112 J固定的affine方程，不宣称当前新H已获真native解。`accepted_warm_steps=1`、`success=false`、`new_coupled_finite_acceptance=false`原样保留。

本附记补充[第79轮正式结论](2026-11-15-actual-request79-twenty-four-query-left465-limit.md)，不等待它完成才允许既定第84轮执行，也不新增数学或数值接受门。
