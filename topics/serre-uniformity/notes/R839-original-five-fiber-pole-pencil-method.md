# 原 D 两锚与 Ey 八生成元：五个既成纤维的最小执行契约

日期：2026-11-16。状态：**执行方法已证明；本消费者尚未运行，未预填1111阶子式。**

数学依据是 [原 D 铅笔与八生成元证明](R839-original-D-pencil-and-eight-generator-pole-ideal.md)。
真实 R842 已取得完整原 $H^0(3H-D)$ 的295维单位解表达式；本方法直接消费该成功产物。
原 $D$ 是 $E_y=\mathcal B+3D$ 中的同一有效除子，$\deg D=395$，
$\mathcal B$ 是原20个 cusp 与 $P_0$，不另选线性等价代表。

## 1. 只做一个新的秩下界

固定辅助素数 $\ell=1000000753$ 和原第0分裂分支。
取 R842 原基 $w_0,\ldots,w_{294}$，定义真正的特征零截面

$$
a=w_0,\qquad b(n)=\sum_{j=0}^{294}n^jw_j,
\qquad n=1,2,\ldots.
$$

系数首先是原单位 chart 的准确解表达式，其当前模值才由 R842 的690行、295列矩阵给出。
不把任意有限域核提升为新的特征零来源。

由完整数学证明，原乘法
$V_3^2\to V_6,(r,s)\mapsto ar+bs$ 的秩为 $1111-\deg Z$，
其中 $D+Z$ 是 $a,b$ 的共同零除子。
因此任意来源正确的1111阶评价子式非零，就证明 $Z=0$。
本消费者只构造节点 $z=0,1,2,3,4$ 的纤维评价矩阵，大小 $1360\times1380$。
无需证明五纤维避免 $D$、纤维约化，或该评价在整个 $V_6$ 上单射。

第一次请求可限定4个整数参数。若均未达到1111，产物只记录这四次模充分检验失败。
它不否定特征零铅笔存在。增加参数上限属于续算控制，不改变数学配置；
已成固定 $a$ 的五个乘法阶段跨所有参数直接复用。

## 2. 七组原源，全部逐字节和完整配置绑定

| 来源 | 本消费者实际使用的内容 |
|---|---|
| R842 | 成功 FINAL、295维原 D 单位核、原830行矩阵、已成 p753 S5 矩阵、元数据与来源审计 |
| R827 | 已成 p753 的1234阶 S5 选行逆、单位网格、前五个原 W/Krylov 纤维及元数据 |
| R787 | 原已成 real-power5 第0000到0689行，原配置及元数据 |
| R786 | 原准确 power5 index、尺度、原配置及元数据 |
| R775 | 原 power4 和 power5 的 recipe，完整 stage SHA 与原配置 |
| R809 | 原 S5 index、原行来源清单及元数据 |
| R837 | 已成原固定21点铅笔、两个准确锚点及其原尺度 |

R842 固定为 run `43776927742`、source
`ccc94341bcab2c33e4732fcb9d6bce517b6243f3`，核心
`6fe0a0d3f37592b1ac3081a8347a205503de41cdd54e41a05529c837a7b3c73e`。
其真实2451、415、395三个秩及295维核只作为已成输入读取。

R827 的原配置同时绑定 R787、R806 和 R809；R842 的原配置再绑定
R827、R809、R786、R837。本核心逐项比较这些真实身份。
R775 旧预算产物与后继完整产物的 power4/5 若来自不同 run，
仅在两个已知原 SHA 完全相同时复用其字节，不能换一个新选择的基。

包装器只用标准库进行 Range、manifest、原 run/core 回执、carrier 和 SHA 核对。
完整数学程序仅在公开 Actions 子进程中导入 python-flint 0.9.0。
本地不得执行矩阵乘法、有限域秩或新的模转换。

## 3. V3 的 normal 转换不生成任何新 Fourier 乘积

原 R775 的 power4 与 power5 前690个 recipe 均为
左因子第0个 $V_1$、右因子同序前一幂，因而

$$
F^{(5)}_j=\tau^2F^{(3)}_j,\qquad 0\le j<690.
$$

直接读取原 R787 real-power5 行；每行的 `R786_row_sha256` 必须等于
原 R786 index 中的对应字节身份。读取原129阶中的前69阶、全部20个实坐标，
不重新执行 $\xi\to t$、相位或实子域转换。

对30个右端一组，使用 R827 已成选行逆求 S5 坐标，逐组代回全部1380行。
原 S5 和右端都保留 $82^{10}$，它们的共同尺度相消后恰有

$$
F_j^{(3)}/\tau^3=\sum_{a=0}^{271}\sum_{k=0}^{3-\epsilon_a}
c_{a,k,j}z^k\beta_a,
\qquad \epsilon=(0,1^{144},2^{127}).
$$

其余 S5 支撑必须全零。这个特征零支撑来自原分次自由基定理；
模零仅检查实际约化没有错位，不能自行替代该定理。
每组保原1380行验证、选行、来源和单位 solve 表达式。
这是690个新右端转换，不重复已成1234阶逆，也不延长 V3 的 Fourier 尾。

## 4. 纤维乘法只用既成 W 和 Krylov 逆

令 $E_c$ 是690个原 $F_j/\tau^3$ 在节点 $c$ 的 $272\times690$ 评价矩阵。
每个节点只计算一次并保存 $K_c^{-1}E_c$。
对候选截面 $s$，先由原 V3 系数得到 $v_s$，再计算

$$
P_{s,c}=[v_s,W_cv_s,\ldots,W_c^{271}v_s](K_c^{-1}E_c).
$$

这正是原纤维环上的 $sV_3$，因为乘法交换且 $K_c$ 可逆。
从旧文件读取的 $W_c$ 与 $K_c^{-1}$ 保原 producer、primitive 元和 normal 基身份。
不形成完整272立方乘法表，不重算 Krylov 逆或原 $W$。

五个 $[P_{a,c}\mid P_{b,c}]$ 依节点顺序堆叠。
实际 rank 等于1111时，保存1111个原行号、1111个原列号以及该实际方阵的非零行列式。
rank 小于1111只记录当前候选未通过充分条件；rank 大于1111会与已证原包含关系冲突，
必须报错，不能截断为预期值。

## 5. 成功输出是原 Cartier 理想 DAG

原 R837 锚点 $u,v$ 的1213阶证书已证明共同零除子恰为 $\mathcal B$。
保其原稀疏坐标、清分母、content 和准确尺度。新1111子式成功后输出

$$
ua^3,\ ua^2b,\ uab^2,\ ub^3,
\quad va^3,\ va^2b,\ vab^2,\ vb^3.
$$

这些 $V_{11}$ 截面在两图分别除以 $\tau^{11}$ 与 $\sigma^{11}$，
给完整原 $I_{E_y}=I_{\mathcal B}I_D^3$。
输出保存原 $a,b$ 单位解和 $u,v$ 原字节来源，交叠乘子为 $t^{11}$。
不要求把八个 $V_{11}$ 坐标展开，不丢任何真实函数常数。

此输出还不是原 $\eta$ 的全部加法映射极除子，也不是 Jacobian 的规范代表。
准确后继恒等式 $I_{E_{y_R}}=(y^2-b)I_{E_y}^3$ 需要原全局 $y$ DAG；
这里按 $I_E=\mathcal O(-E)$ 的嵌入乘 $y^2-b$，不取其逆。
本消费者不把已成 CM 点值 DAG 当作该函数。

## 6. 文件、标签与恢复

核心：`scripts/R839_original_pole_pencil.py`。
RESULT：`R839-original-D-pencil-and-eight-generator-pole-ideal`。
FINAL：`p41-original-D-pencil-and-pole-ideal-certificate.json`。
CLI：`--config <expanded-job> --out <output> --budget-minutes <300>`。

数学配置包含新核心 SHA、冻结 helper SHA、证明和本方法 SHA、七组原来源的
完整身份及所有选入文件字节、固定素点/节点/基次序/候选规则。
绝对路径、预算、参数上限不进入数学身份。

阶段均为根目录 `R839-pole-*.json.gz`，先原子写后登记。
主要阶段为来源审计、23个 V3 转换组及 index、五个纤维、候选截面、
固定 $a$ 五组乘法、各 $b$ 五组乘法、各实际 rank 和最终八生成元 DAG。
stage manifest 列全部已成阶段，不列它自身；中断的临时文件不列入。
同标签的已成阶段原样复用，false FINAL 只是一条历史结束记录，不覆盖较晚阶段。

成功 FINAL 必须同时给
`complete_original_D_pencil_certified=true`、
`complete_original_Ey_ideal_certified=true`、
`actual_pencil_rank=1111` 及准确参数和 DAG 引用。
预算或有限候选停止时 `complete=false`，保存全部已成阶段供同源续接。
`expanded_characteristic_zero_coordinates_computed`、
`Jacobian_standard_representative_computed`、`actual_eta_or_height_computed` 始终为 false。
可重现的原矩阵和新阶段只在一日 artifact 中续传；Git 仅留脚本、请求、方法与实际 metadata。
