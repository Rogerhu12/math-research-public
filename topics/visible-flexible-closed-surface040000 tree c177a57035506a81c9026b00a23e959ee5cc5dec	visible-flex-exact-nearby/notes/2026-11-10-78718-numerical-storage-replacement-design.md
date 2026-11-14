# 新 78718 纯存储替代：定义、最小改动和待审范围

状态：**事前设计；当前执行见[来源适配与reader检查](2026-11-10-78718-storage-adapters-and-reader-check.md)，完整独审未完成、未用于生产**。这是原 A/B 字节无法从已检查材料恢复后的新来源，绝不称为原 A/B 的恢复。原单容器支路仍优先；run02 及其所有绑定来源不改。设计不运行新 ODE/PDE，也不调整任何曲面参数、节点、模式或数学验收条件。

## 1. 精确的逻辑对象

把原 `950f-root-fullxyz-hermite.py::build` 或 `db6f-root-mirror-hermite.py::build` 中**完全不变**的 `np.savez` 调用产生的 NPZ 字节记为 $Z$，把其原语句 `gzip.compress(Z, mtime=0)` 的输出记为 $P$。这里逻辑容器明确是“原 gzip/NPZ 字节流” $P$，而不是重序列化后的数组。原 `data_sha256` 继续指 $P$ 的 SHA256，因此原数据身份有精确、可核对的延续；另一个新 descriptor 身份只描述它如何存储。

只把 $P$ 切成按偏移连续排列的块 $P_i$，每个原始块至多 4,600,000 B；每块独立 gzip。写盘前检查每件实际压缩文件严格小于 5,000,000 B，JSON 索引小于 1,000,000 B。完整 $P$ 和 $Z$ 只在内存中出现，不能先写超限的大文件再拆分。

### 字节等价命题（纯代数证明）

设 $P$ 是任意有限非空字节串，分片覆盖区间 $[0,|P|)$，没有间隙、重叠或重排，每块解压后的字节等于相应 $P_i$。则

$$\operatorname{concat}_i\operatorname{gunzip}(\operatorname{gzip}(P_i))=P.$$

证明：gzip 的无损性给出每个分片的逐字节等式，区间分割保证连接次序逐字节覆盖 $P$，故连接串与 $P$ 相同。程序还核每件 stored/raw 长度与 SHA、全局长度与已绑定的 logical SHA；这些检错标识不替代上述无损等式，也不把 SHA 无碰撞当数学公理。

对相同 NumPy 读取代码、相同 $P$，读取输入的全部 NPZ 头、dtype/shape/Fortran 标志和数组字节都相同。这保持包括有符号零、NaN payload、字节序和空维度在内的位模式。编码器不得做浮点运算、dtype 转换、数组重排或 `np.savez` 重写；生产器原有的转换及 mirror parity 修改仍各执行原来的语句一次，不因存储迁移改变。

### 同一有限曲面命题（条件性）

若 producer 的全部数学语句和原 NPZ 序列化调用保持原样，且 reader 只把“从单个文件得到 $P$”换成上述字节重组，那么 reader 的 mesh、三个导数层（0、1、2）的 nodal two-jets、每段 mean increments 的 binary64 位值逐项相同。原 Hermite、Fourier、精确和式、common-cut、区间舍入、metric/moment/标量预算和网格公式全部保留时，它们定义同一有限图；这不是原图满足任何误差界的新证明。此命题要由完整文本差分和消费者闭包审查支付，不能只靠 codec 单测宣告成立。

## 2. 新来源与最小改动

所有新文件用 `78718-prefix-*-storage-v1.py` 或 `78718-prefix-byte-shards-v1.py`，不覆盖旧文件。

| 来源 | 只允许的适配 |
|---|---|
| 新 stdlib byte codec | 连续分片、gzip、完整字节重组、长度/SHA/文件限额；不导入 NumPy |
| 新 stdlib storage helper | 显式 `data_storage` envelope；原 logical `data_sha256`；hash-only 入口；可选原 NPZ 三数组布局读取；返回实际 descriptor/parts/helper/codec 闭包 |
| 原 fullxyz producer / `SharedHermite` | 原 NPZ 序列化后改写存储；constructor 的逻辑容器获取；新 source 身份 |
| 原 mirror producer | 原读出和 parity 语句保持，改写后的 NPZ 走新存储；两次 payload 用 hash 命名避免覆盖未知片件 |
| 原 `ExactHermite` interval reader | 构造函数的载入层和 storage bindings；原区间/有理数/三角函数全部保留 |
| 原 polynomial / supplier / moment | 指向新 reader；报告补实际 prefix storage 闭包；它们自己的 target 数组存储不改 |
| 原 common-cut v2 | 两处直接读取 base NPZ 改走**定义 base** 的 storage helper，绝不拿扩充后的 common-cut 模数解析 base；原公式和 tail reader 不变 |
| 原 prefix budget / tail arithmetic 的独立 prefix 副本 | 新 prefix 副本只更换导入，避免改动原 tail backend；所有算术函数保留 |
| 原 closed budget v3 | 明列新 common-cut/interval reader，报告 prefix storage 闭包；原 transfer-v3 来源和标量不等式不变 |
| 已恢复 C angular / terminal / mesh / review | 在新身份副本中替换完整 prefix source pins 和实际路径；保留原 tail/source/M12 reference 家族，补齐新 prefix 闭包。原 C 历史身份不改。 |

每个派生文件的全部文本变换按顺序保存，要求每一步旧片段唯一出现，最终全文 SHA 匹配。对无存储改动的数学函数再逐个比对 AST/原文；对含读写代码的函数，逐段列明唯一载入/写出及来源报告替换，不忽略剩余函数体。

## 3. 必要复核

1. 通用字节 codec：确定性合成 NPZ，含标量、空维度、多维 C/F 布局、非本机字节序、NaN payload、正负零、无穷与整数/复数；比较原/重组容器的完整字节，再比较原 `np.load` 的 dtype/shape/顺序/数组位串。
2. 真正跨 4,600,000 B 的高熵 payload，检查每个真实盘上片件、偏移/覆盖与限额；整容器只留内存。缺片、重排、偏移、长度、SHA、路径、重复 JSON 字段等损坏必须拒绝。
3. 显式 helper 的实际磁盘来回和 relocatable 闭包；hash-only 子进程不导入 NumPy/SciPy。
4. 原与新实际 reader 对同一小型合成 three-array prefix 的读出与系数等价。synthetic NaN 的位值保持由纯读取层检查；原 interval reader 对非有限输入的拒绝保持。不能以新的数学对象或借用旧证书充当该测试。
5. producer 完整文本 replay、保留所有数学语句/NPZ 调用和实际消费者 source pins；C 终门必须真的沿新 descriptor/parts 读逻辑字节。未完成完整闭包和独审，不能称生产可用。

## 4. 当前未支付事项

core合成4正/23拒、14适配完整唯一文本replay及实际两reader/终门存储子程序检查已完成，
准确源码/回执见上链接。完整134替换及真实消费者闭包独立审查待完成。没有新曲面、metric/reach/尾证书、网格或 G5 结论。独审由未参与优化的 independent_audit 在 root 排定优先级后完成，原数值独跑资格不变。
