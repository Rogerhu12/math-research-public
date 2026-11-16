# 三曲率原子完整五门：真正新模型的执行边界

本次沿 [R491](../results/R491-complete-complex-phase-and-two-curvature-atom-five-condition-boundary.md) 和 [R493](../results/R493-three-curvature-atom-five-parameter-formulas-and-regular-zero-lift.md)，直接计算三曲率原子及远左常数 C 的五个实参数模型。旧十五参数正曲率 cap 的六起点任务已经结束；本次不读取其旧数值点、积分前缀、Jacobian 或日志。

## 模型与原条件

参数为 0<a1<a2<1、0<b1<b2<1、C>0。使用完整十二项密度、八个累计 Aj 和原五个 Delta1/2/3/4/6；所有段都是最高21次的有限单项式原函数，包含全部移动端点、Ci、taui、H 和端点势。五乘五 Jacobian 同这些完整公式解析传播，不以 E 两条件代替五条件，不用单侧值乘 delta 替代 r 跳变。

搜索 chart 为 a2=q2、a1=q1*q2、b2=q4、b1=q3*q4、C=exp(z5)，qi=sigmoid(zi)。前四 z 在 [-4,4]，末项在 [-8,3]。36固定起点：q1…q4 为 (1/4,3/4) 的16个字典序组合，每个配 C=1/32、1；再取所有 q=1/2 配 C=1/128、1/8、1、8。每起点最多120 nfev。残差 Fnu=(1+H)^(nu/2−4)Gnu，Gnu=Deltanu/R5；原未缩放 G 一并保留。

## 同一费用账及真零门

从脚本最初的 monotonic clock（包括 imports、输入、失败和输出）起最多120秒、5000次完整值与解析J。搜索在105秒停止。首个原 G 无穷范数≤1e−8 的点才进入同一费用账内的80位 Decimal Newton，最多8次；随后精确160位二进有理中心、128位有理逆，以及半径 2^-16、2^-24、…、2^-72 的8个盒。只有有理有向界证明 q<1 且 eta+q*r<r，才叫严格内部正则真零。浮点小残差、优化器返回或只读摘要完成都不是五门真零。

若真零门通过，R493 仅授予参数 C1 正曲率平滑与有限 IFT 得到真正光滑五门零 cap；共同母库、真实全路径、同规范和主几何 README 完成标准仍须继续。若有限搜索没有真零，只报告本模型本起点本预算的观察，不作 cap 不存在结论。

## 源码与输出

- 科学源码 `scripts/literature_three_atom_cap5_search.py`：41769 B / af7b497b3b8f94846fb05947bf028b50c9811e3eb37d25acf18e59ea48a55fbc。
- 只读源码 `scripts/observe_three_atom_cap5_stdout.py`：15663 B / 9bf7cdac0eadb602f0cb60282a9ef95af323f288db1632f2489afdaec7077385。
- 固定原 reader：50679 B / b7b16d0917bf99e4183421ab6d5c1dd33b9c0fe8009ad59a5141a17d798e5c4a。
- 新请求 `computations/request-three-atom-cap5-search.json` 及工作流 `.github/workflows/visible-three-atom-cap5-search.yml` 绑定各源码身份。
- 科学输出只留公开 Actions 原 stdout 和临时 runner 文件；无 artifacts、Release、Git 数组或跨 run 缓存。32 MiB 软输出门会停止继续研究，不能用多件拆分转存。

report job 只下载一次已完成 research job 的原 stdout（上限40 MiB），允许 workflow 自身尚运行、research 原结论为失败。保原 raw 字节数/SHA、原失败、优化返回、候选/证书及全部 FINAL_REPORT/FINAL_CLOCK；普通 oracle 全值/J 留原stdout，只摘身份、种类计数和首末seq。4 MiB摘要不完整时明确失败，不补研究成功。

每个job执行前实际 public/private pull，根/题 README 变化只读差异即按新规停止旧执行安排；private token 在科学入口前移除。QUEUE本会话维持进行中。此次是继续研究，不是主课题收尾。
