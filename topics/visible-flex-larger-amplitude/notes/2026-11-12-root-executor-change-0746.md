# 07:46 UTC执行器切换与恢复

2026-11-12，root，GPT-6 Astra Pro，AI-assisted。

## 可观察事实

07:45前原工作区可读写；07:46新exec报No such file or directory，既有会话94301/73042的poll报executor key changed during session recovery。后来使用shell=bash、login=false、cwd=/恢复新终端，但原仓库/source/未提交文件均不再可见，只有刚经apply_patch新写的恢复note。不能据此补出失联作业退出码。

07:50在math-research-recovered重clone/checkout/pull main，HEAD7f2191d504f55128229357b5dea992c1176f931a；两README对已读303483ad1fbbb86a193074c2b5c588334f2d8c7d均无差异，HANDOFF已登记。最近完整已推源1d98a1198f95546c6954773ae5cfaa2667346b89，发布b319844100297e5f067912b1e0abe860367fab22。新source仍固定869436630c99aa5a68afb55bd8877c826034d117，用91件SHA manifest恢复。

## root已经重做

真实Rout积分v4原源码SHA bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe已逐字恢复。原session3203曾正式exit0，94.57631229s/30440KiB，但其未推数值文件现不可访问。新session39503重新执行全部12外层、108段、304panel，正式exit0，5.420717389s/31256KiB；新文件root-real-outer-radius-v4-recovered-full.json及新解析核对包均存在。结果仍为Rout=.30000000000000715908123386±6.70e−27，减binary.3严格正7.1701834641e−15±9.97e−27。源码与R26完整证明一同提交。

旧v1整条session60197由owner中止exit130，只完成11..3；旧v2/v3分别在cell2访问预算耗尽，未收cell2；这些未推日志/源快照失去访问，不能重新制造其原字节。现在直接重做完整v4，不把旧部分成功替代全条。

## root尚待恢复

已推actual M20 resume1的raw（ef36aff558beb340e35f6ac84bfd3abe893186604abb8dd4d9d85bbebcfafb39）和首完整tail response（95147d132e0c0662cae3e360f977f0759cf4080ce60272ce702d38039f6a07e9）仍可取。raw的911节点inner RMS9.97554535390274e−7，但第二true-DN worker−9，不是物理验收。独立staged audit45361 worker−9，也不成功。

未推compact首试1124是worker替换锚点错误，旧源码52caf6c4ef0717531fa4e59367965bdcd0df9e310289770e6a00c8b9d41b3ad0已在b319；修正为唯一子串const sol=dn.solve(req.height,即可，不改变方程。compact-r1会话81631外层exit1，初始化无ready；未捕获worker自身退出码，禁止记作−9。其wait4峰237272KiB、过程树样本峰264788KiB均不是OOM证明。后续client异常捕获/进程采样器及stage --storage/--reference-adapter选项尚未推，要重建或由新的冻结校准adapter替代，保留物理配置等价核对。

恢复验收仍要求完整同一H的实际非线性tail响应（jacobian+audit）、原RMS及真实BC门，不能直接翻raw成功旗标。旧M16恢复适配器逐位RMS/BC检查已推可复算。

## 并行分工

strong恢复原子Newton保存/恢复、小batch有限差分诊断和冻结校准factory；r1真BVP从未启动。exact恢复真实low46及Green源码并重做M8/Green/46，旧73042无终态。tail恢复R31完整背景证明、R32完整展开/填盘证明，再继续R33。所有未推成功包真实重算；只有文字摘要的仍标待恢复。Node/大BVP串行，低内存Arb可并行。

课题完成标准仍未满足，持续推进，不在本恢复记录停止。
