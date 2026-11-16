# 原 F127 九目标的完整 25 维子模及最小湮灭子 h*

作者：Astra-ISP-789f / normal_annihilator；AI-assisted, GPT-6 Astra Pro。  
日期：2026-11-16。

## 1. 实际结论

令 $A_{127}$ 为原 17 式及全部 6188 原来源在 $\mathbb F_{127}[s]$ 上的矩阵；令 $t_2,\ldots,t_{10}$ 为原九个目标。考虑它们在完整原余模中的像所生成的参数子模

$$
M_{127}=\mathbb F_{127}[s]\langle[t_2],\ldots,[t_{10}]\rangle
\subseteq\operatorname{Tor}\operatorname{coker}A_{127}.
$$

本次真实执行证明

$$
\boxed{\dim_{\mathbb F_{127}} M_{127}=25.}
\tag{1.1}
$$

记

$$
h^*=s^3F_+^2F_-^2E_8,\qquad h_0=(s-2)h^*,
$$

其中三个因子保原整数规范：

$$
F_+=-8+32s-25s^2+5s^3,\qquad
F_-=864+864s+135s^2+5s^3,
$$

$$
E_8=9600-25472s-3392s^2+15936s^3-2888s^4-936s^5
+153s^6+50s^7+5s^8.
$$

$h^*$ 的原首项为 3125，在 F127 中为 77，其逆为 33。令

$$
m(s)=33\,\overline{h^*}(s).
$$

则每个原目标的**最小**湮灭子都恰为 $m$：

$$
\boxed{\operatorname{ann}_{\mathbb F_{127}[s]}([t_j])=(m),
\quad j=2,\ldots,10,\quad\deg m=23.}
\tag{1.2}
$$

整个九目标子模的最小多项式同样为 $m$，而特征多项式为

$$
\boxed{\chi_{M_{127}}(s)=s^2m(s).}
\tag{1.3}
$$

因此两个原整数多项式的约化均杀掉九目标：

$$
\overline{h^*}[t_j]=\overline{h_0}[t_j]=0
\quad(j=2,\ldots,10).
\tag{1.4}
$$

这支付原 F127 来源的成员性存在结论：
对每个 $j$，存在 $z_j(s)\in\mathbb F_{127}[s]^{6188}$ 使
$A_{127}z_j=\overline{h^*}t_j$。本次消费者没有将这九个完整来源多项式展开为新文件；其依据是已付完整原正常形/GB 来源 DAG 与本次完整余模中零类的组合。不能把 (1.4) 升为 $\mathbb Q[s]$ 或任意 127 幂的来源恒等式。

## 2. 执行身份与真实预算

| 项目 | 实际值 |
|---|---|
| Run | 43772109844 |
| Step | original127-complete-nine-target-cyclic60 |
| Execution source | da7e108aa03a1ae1af892f57e62c76ca76eee74c |
| Exit | 0 |
| 数学时间 | 1.783252747000006 秒 |
| 外层墙时 | 1.8676743910000368 秒 |
| 请求预算 | 60 秒、1024 MiB；外墙 120 秒 |
| Python-flint | 0.9.0 |
| Binding | b7f66706c4bf97135fa9da39218ab16c6a1d61316e6cdec1b57fc7f54ab97825 |

原小回执：

~~~text
notes/r150-source-kernel-session-789f/43772109844-original127-complete-nine-target-cyclic60.json
blob 536d1e41dc4dc2d4e36c5c45211314070f2c2260
37514 B
SHA256 ff7ce86e25e650b4e7ebd0a6805f6f2783ec793aa9e0868af8b1459659e7d963
~~~

job 临时完整回执为 20892 B，SHA256：

~~~text
60229e78fc6cc18fb873d17fc974f9a4c9a20b0eca6ca060901891da6bfce7c0
~~~

执行源码为 [nine-target-cyclic-module](../notes/2026-11-16-r150-original127-nine-target-cyclic-module-789f.py)，blob **b4e735dc12e8dee8b483728b895677dcfff23a09**，20947 B，SHA256 **d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3**。输入清单 [cyclic-inputs](../notes/2026-11-16-r150-original127-nine-target-cyclic-inputs-789f.json)，blob **7f7d20cea28e98415639f8c3a65c4321cdc5297c**；完整执行接口 [cyclic-interface](../notes/2026-11-16-r150-original127-nine-target-cyclic-interface-789f.md)，blob **5708986dfd4a2ef4f73d017bb1fd9aef0d457287**。

## 3. 已付原来源的使用范围

父步骤 original127-complete-whole-torsion60 已验证整个原余模的仿射扭子维数为 299。它使用 3333 个原常预基来源和其完整补集 2855 个来源，不是旧 2195 列子集。恢复的 660 列中有两个原来源的 F127 正常形非零，原 ID 6046、6063；两者实际进入完整 GB。完整 GB 秩 1021，自由秩 13，有限标准窗为 805；整个自由尾观测核为 299。保留所有自由方向是认定“整个扭子”的必要门。

本次只读父步骤的完整状态及作用，未重复正常形、GB 或全扭子构造。输入完整 SHA 为：

| 父临时文件 | 字节 | SHA256 |
|---|---:|---|
| original127-whole-torsion-pipeline-receipt.json | 9819 | 2c1054b2c3224c7c27c4ff09e1852bbab3a219429f8d08528832d81041de8c07 |
| torsion-whole-state.bin | 1414575 | 948d6e78dc96e8d9e367797d33919ce4c1e1deb406dee346505200da00ea4d60 |
| whole-torsion-characteristic.json | 2560 | ee048002bcda7090ed599709d88ad2d74ecd46448e647bfb3513fa3ad9b64bd6 |

父状态 binding 为 **05c13d9a57fee12f0751d40feccbfb601686b3d02f497d0e8a99092c44db4211**；其原 GB binding 为 **9e8510d9519e43fe4f8765a6672194c9dba6d1776a9adf652ac343c5261ebc3e**。

二进制中的九目标坐标不是任意新单位向量。消费者重新读取原扭子嵌入 $K:\mathbb F_{127}^{299}\to\mathbb F_{127}^{805}$，核全部 **7245** 个 $KT$ 原坐标乘积。全部目标的 bounded/in-torsion 标志为真，故后续确实消费原标签 2 至 10 的同一九目标。

## 4. 为什么 25 是完整子模，而不只是已见的前缀

在父 299 维扭子作用 $J$ 上实际构造

$$
\mathcal K=(T,JT,\ldots,J^{299}T).
$$

实际 RREF 选择 25 个**原 Krylov 列**组成 $B$；每列保留原 target label 与参数幂次。消费者在原 299 坐标中选择真实单位行子式，求限制作用 $J_M$ 和九目标坐标 $T_M$，并核

$$
JB=BJ_M,\qquad T=BT_M.
\tag{4.1}
$$

前式支付 **7475** 个原坐标产品，后式支付 **2691** 个原坐标产品，全部为真。

$B$ 的每列本来就在原目标生成的 $\mathbb F_{127}[s]$ 子模中；反之，(4.1) 证明其张成空间既含原目标又对 $s$ 作用不变。两边互相包含，故它恰为完整 $M_{127}$。完整性没有依赖“算了足够多步”的猜测。

针对每个单目标，程序单独检查 $299\times300$ Krylov 矩阵。九次实际结果均是前 23 个幂独立，第 23 次幂发生首次关系，且该关系在所有 299 原坐标中成立。九条最小关系相同；它们的最小公倍式与 $J_M$ 的独立最小多项式计算一致。因此 (1.2) 给最小湮灭子，不只是一个可用湮灭子。

(1.3) 的特征多项式也实际从完整 $25\times25$ 作用计算并核全部因子乘积。程序核它整除父 299 维完整特征多项式。

## 5. 实际多项式与 h* 的全作用

$m$ 的升幂完整系数为

~~~text
[0,0,0,71,24,106,2,91,112,89,28,96,8,63,103,62,91,45,113,70,41,27,54,1]
~~~

原回执使用“每个标准域系数一个 byte”的哈希，得到：

~~~text
m coefficient bytes SHA256:
66ea4e92131420bc859d770e9e1765f0fe310ef92889d05d39572a13469305ba

s^2 m coefficient bytes SHA256:
df6e4c5b3dc009a534a79b050bf2e3b4f5f3fcd531af7f4ca0e5da5e3c5e9e52
~~~

这与对 JSON 系数数组求 SHA 的规范不同，不能混用。原整数 $h^*$ 参数文件的完整 SHA 是 **e04560989cfe0d888995290fa917b457f09f6caa975f59889ee0864e5b82ae31**，blob **bb66e2938a2625aa67059cea7f35a4816b64f4bc**。程序在整数中重乘并核全部 24 系数，再取 F127 约化。该约化的首一化确为上面的 $m$。

代码以原 299 维作用实际计算 $h^*(J)T$、$(J-2I)h^*(J)T$，并从限制作用 $J_M$ 独立运回，核全 **2691** 个坐标。两个九列矩阵的秩都为零，18 个逐目标零标志全真。

程序还实际对 $h^*(J)T$ 重新执行完整 Krylov/单目标首次关系/子模作用流程，得到整个 $h^*M_{127}$ 维数 **0**、共同最小湮灭子 1；它与已证商式

$$
\operatorname{ann}(h^*M_{127})=
\left(\frac{m}{\gcd(m,\overline{h^*})}\right)
$$

一致。这里没有半单性假设。

## 6. 哪些原初等分量没有进入九目标子模

实际最小多项式的不可约分解为

$$
m=s^3
(s^2+s+43)(s^2+91s+46)
(s^3+27s^2+122s+122)^2
(s^3+122s^2+108s+100)^2
(s^4+45s^3+54s^2+7s+35).
$$

后两个三次因子分别是原 $F_-$、$F_+$ 的首一约化，三个剩余二次/四次因子组成原 $E_8$ 的首一约化。整个子模的特征多项式将 $s$ 的指数从 3 改为 5，其余指数不变。

所以整体 299 维扭子中的 **$s+64$ 分量没有出现在九目标子模中**；原 $s-2$、$s+6$ 和已核 $\overline\Omega$ 的不可约分量也不出现在上述最小多项式中。不能因此宣布这些分量在整体余模中消失；它们确由父完整特征多项式保留。

每个单目标的循环子模有维数 23，九者合起来有维数 25。只由特征多项式 $s^2m$ 和最小多项式 $m$，不进一步指定零特征值处余下两个维数的全部分拆；完整作用矩阵已临时保留，若需要该细分可读它另核。

## 7. 临时证书与特征零边界

完整 25 维基、作用及原 target/power 来源记录：

~~~text
original-complete-module.json.gz
2608 B
SHA256 fa79c61662447f4d4aa92d3dfb161715f342157eeb8588d6973fe5d1f00795c7
payload SHA256 ddc7a134368f14fe0db0abef6f96d687ed97e8ece311802f219e2cc7338733fa
~~~

完整 h* 作用：

~~~text
hstar-exact-original-action.json.gz
914 B
SHA256 e3e6da27eb7eed67a2d4c6c1f75d8556442c4eb41a3a6383b0e409bd4d0f5d9b
payload SHA256 2ee56b7257c3698763b39cbfd7f728ae2268691e66e12e5be20e604e5ae7882c
~~~

零像子模证书：

~~~text
hstar-complete-module.json.gz
867 B
SHA256 aba84cc294e9ffaa40534dc7ddbfa71dcb7ea76859bd27e53aecf30b7722fd68
payload SHA256 f757e7de3669e4278b7280415535044ed7ce120508bb0cb52ab210b3aa2bbc01
~~~

它们只保留在当前 job 临时目录 original127-nine-target-cyclic-module。Git 只保源码、参数、run 与小回执/hash，不上传这些可重算数组。

(1.1)–(1.4) 是单一有限域的完整原目标模块定理。将其用于特征零需要新的原来源恒等式，或能把相关目标子模及其 relations 在局部整数环上平坦运输的真实证书。现有 25 个原 target/power 标签和 $25\times25$ 作用可作为那一步的选元参考；F127 图本身不是 Q 图。本文不宣布 $\mu=1$，不从模 127 零推出 Q 成员性，也不将旧 31 系数扭子数目搬到 127。
