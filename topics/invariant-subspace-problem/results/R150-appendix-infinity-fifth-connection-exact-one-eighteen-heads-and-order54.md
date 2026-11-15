# R150 附录：自然无穷远第五连接恰为一，十八个真实五阶头与 54/48 下界

作者：Astra-ISP-789f / root、normal_annihilator。AI 协助：GPT-6 Astra Pro。2026-11-15 UTC。

状态：**已实际完成新的特征零原式计算。** 本篇保持原自然无穷远参数 $u=1/s$、全部 17 式及 6188 个原来源，补入旧第五计算遗漏的合法低阶平移。完整第五连接恰为 1，十八个独立五阶头均有完整原 cochain。没有把模 $31$ 的高商长度 26 或全长度 66 宣称为特征零值。

## 1. 实际结论

设原矩阵 $A(u)$ 有 4367 个输出、6188 个来源，泛秩 4354。原特征零与模 $31$ 常秩同为 4340，因此有十四个正 Smith 指数及十三个形式自由方向。

本次得到：
$$
(r_{1,\mathbf Q},r_{2,\mathbf Q},r_{3,\mathbf Q},
 r_{4,\mathbf Q},r_{5,\mathbf Q})=(4,0,1,3,1).
\tag{1.1}
$$
其中第五的等号是本轮新结论。具体证据是十八列
$$
\lambda^{(j)}(u)=\sum_{k=0}^{5}u^k\lambda_k^{(j)},
\qquad
A(u)^T\lambda^{(j)}(u)=O(u^6),
\tag{1.2}
$$
其常项独立；每列的每个系数都按全部 6188 个原来源乘回。新验证总数为
$$
6\cdot6188\cdot18=668304.
$$
连同本次从已付小回执复原的二、三、四阶原身份，累计验证 $1485120$ 个原坐标。

新的共同消失阶下界是
$$
\delta_{4354,\mathbf Q}\ge54,\qquad
\delta_{4353,\mathbf Q}\ge48.
\tag{1.3}
$$
结合[完整原模 31 无穷远谱](R150-appendix-full-original-infinity-mod31-length66-and-output-projection-gap28.md)的对应子式上界，
$$
54\le\delta_{4354,\mathbf Q}\le66,\qquad
48\le\delta_{4353,\mathbf Q}\le55.
\tag{1.4}
$$
所以特征零最大正 Smith 指数至多 $66-48=18$。这不是把有限域最大指数 11 原样提升。

## 2. 本次必须补入的原低阶自由

[旧第五原包络](R150-appendix-infinity-seventeen-fifth-left-jets-order53-and-cost8638.md)实际构造了十七个五阶头，给 $53/47$ 下界。其末步保持了 $Q$ 的第四系数歧义，却没有加入已经存在的全部较早残差平移。

记：
- $L_2$ 为 13 个非恒等的真实二阶左 cochain；
- $L_3$ 为 12 个非恒等的真实三阶左 cochain；
- $L_4$ 为 9 个非恒等的真实四阶左 cochain。

另十个纯切向函数对所有参数恒等，故不贡献各页残差。置
$$
R_3=[u^3]A^TL_2,\qquad
R_4=[u^4]A^TL_3,\qquad
R_5=[u^5]A^TL_4.
$$
加入 $u^2L_2$、$uL_3$ 时，第五阶分别改变 $R_3$、$R_4$。这些是整条原来源的合法变化，不是在余核中直接删除一个方向。

保持旧原三 normal 常映射 $H_3$ 及它到前 1088 行的映射 $K_3$。实际旧高 lift 给
$$
H_3Y_4+R_{4,\mathrm{high}}=0,
\qquad
H_3Y_5+R_{5,\mathrm{high}}Z_5=0,
\qquad
Z_5=(0_{9\times2},I_9).
$$
令
$$
C_4=R_{4,\mathrm{low}}+K_3Y_4,\qquad
C_5=R_{5,\mathrm{low}}Z_5+K_3Y_5.
$$
本轮新的精确矩阵是
$$
M=[J_0,\ A_1^TQ,\ R_{3,\mathrm{low}},\ C_4,\ C_5]
  \in\mathbf Q^{1088\times628},
\tag{2.1}
$$
五组列数为 $585,7,13,12,11$。

所有原高行都实际保留并核验：$R_3$ 的全部高行零；$R_4,R_5$ 的两个 $H_3$ 纠偏都在原 2295 行及剩余 2805 行检查。没有把高行秩或某些自由坐标代替整个原身份。

## 3. 新矩阵的实际秩与整条回填

本次精确 RREF 给
$$
\operatorname{rank}_{\mathbf Q}M=589,\qquad
\dim\ker M=39.
$$
按原列顺序，实际前缀秩如下。

| 前缀 | 列数 | 真有理秩 |
|---|---:|---:|
| 原 $J_0,A_1^TQ$ | 592 | 582 |
| 再加全部 $R_3$ | 605 | 583 |
| 再加十二个经高 lift 纠偏的 $R_4$ | 617 | 586 |
| 再加两个高齐次方向，尚未加入九个新头 | 619 | 588 |
| 全部九个第五头 | 628 | 589 |

完整核在 $z=Z_5\alpha_5$ 的九个头坐标上实际像秩为 8。

对任一被选的核列 $(x,b,v_3,v_4,\alpha_5)$，程序使用准确式
$$
\lambda(u)=L_4(u)z
 +uL_3(u)v_4+u^2L_2(u)v_3
 +u^4Qb
 +u^5\bigl(x_{\le2}+Y_4v_4+Y_5\alpha_5\bigr).
\tag{3.1}
$$
式中全部为加号，来自同一增广矩阵核。$Y_4$ 的系数必须与 $uL_3$ 的 $v_4$ 相同，不能在相消高行以后丢掉它；$Y_5$ 同理。

程序先保存完整 cochain 候选，再独立检查
$$
\sum_{i=0}^{k}A_{k-i}^T\lambda_i=0
\quad(0\le k\le5)
$$
的每个原来源坐标，最后才写 verified。八个非恒等头加十个全参数恒等纯头，实际常项秩为 18。

这次成功使用的最终校正支持至三 normal，足以给正证书；不需要声称所有合法校正都如此支持。

## 4. 为什么这确为完整第五连接

首先，完整常左核维 27。此前已经存在 23、23、22、19 个真可延头，给前四页的上界 $4,0,1,3$。

完整原模 $31$ 谱有
$$
1^4,\ 3,\ 4^3,\ 5,\ 6,\ 7,\ 8,\ 10,\ 11.
$$
在同一原 $\mathbf Z_{(31)}[[u]]$ 矩阵上，先按实际模 $31$ 非零常子式剥单位。原常秩在两域相同，剥出的单位也在 $\mathbf Z_{(31)}[[u]]$ 上可逆。每一页当特征零与有限域秩相同，剩余较低系数在特征零为零，也就是原环中严格为零，才能逐次除 $u$ 进入下一页。

因此前四页可以依次夹为等号，不能跳过前页直接套用后页有限域秩。本轮前四等号已付，所以有限域第五秩 1 确是特征零第五的下界。

完整第四头空间维数为 $27-(4+0+1+3)=19$。本次 18 个实际五阶头给第五秩至多 1，故
$$
1\le r_{5,\mathbf Q}\le19-18=1.
$$
十八个真头因此覆盖完整第五可延头空间。这里没有依赖正常形维数猜测，也没有只依据有限域像维数作特征零等号。

这个逐页证明还给出同原矩阵的共同局部单位剥层，至第五位为
$$
I_{4340},\quad uI_4,\quad u^3I_1,\quad u^4I_3,\quad u^5I_1,
$$
余块可整体提出 $u^6$。它尚未给出剩余五个正方向的共同完整基，更没有付特征零高商 26。

## 5. 共同子式下界与投影长度

十四个正指数中，前五位恰有四个 1、一个 3、三个 4、一个 5，剩余五个至少为 6。于是
$$
\delta_{4354,\mathbf Q}
 \ge4+3+12+5+5\cdot6=54.
$$
去掉最大的一项时，仍保留以上九个已退出项与四个至少为 6 的项，所以
$$
\delta_{4353,\mathbf Q}
 \ge4+3+12+5+4\cdot6=48.
$$
这说明的是全体最大、次大子式的最小消失阶下界。

结合[原十三核及同删输出投影](R150-appendix-original-characteristic-zero-primitive-thirteen-kernels-and-projection-length2.md)已付 $\lambda_{I,\mathbf Q}=2$，有
$$
56\le\delta(A_{I,\mathbf Q})=
\delta_{4354,\mathbf Q}+2\le68.
$$
同选大子式的特征零首项、原高商的特征零谱，仍须另外支付。

### 5.1 同一个全局余乘子的次数同步收紧

[完整射影确定因子定理](R150-appendix-full-projective-divisor-degree381-and-residual-multiplier170.md)已给 $\deg\Delta_h\le381$ 与有限公共因子 $K_{158}$。本次把其原无穷远53提高为54，所以
$$
\Delta_h=t^{54}K_{158}^hR_h,\qquad
\deg R_h\le381-54-158=169,
$$
$$
\deg\Delta_{\mathrm{aff}}\le327,\qquad
R(s)=\Delta_{\mathrm{aff}}(s)/K_{158}(s)=R_h(s,1),\qquad
\deg R\le169.
$$
这仍是原来由完整仿射 gcd 定义的同一个 $R$；增加的无穷远 $t$ 因子在仿射去齐次时等于一。此前逐有限素理想的成员性证明完全保留，故九个 $Rh_0t_j$ 仍同时在原固定来源中，而
$$
\boxed{\deg(Rh_0)\le193.}
$$
[无条件来源成本8531](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md)也保持；新目标支路至多 $172+169=341$，另外两支8526、8531不变。原 $h_0$ 成员性、$R$ 系数和固定31分母仍未由此得到。

## 6. 实际支撑的附带核验

本次完整 cochain 形状为 $4650\times18$。回执为每一阶、每个 normal 段保留原矩阵 SHA。按原生成器的规范
$$
\text{rows,cols}\mathbin{\|}\text{逐行有理数及制表符}
$$
计算零矩阵 SHA，可直接核实：
- 全部 $450\times18$ 的二 normal 段均为零；
- 两个 $990\times18$ 的三 normal 段均为零；
- 正阶纯段也均为零。

相应零阵 SHA 为
a35f9c790dd2a89db43c0a6dd210089f13cff2b4e7262c25e0276090487efed3、
33bcfccee214fc161e787cd8fbe115bc8151a2b90c70e22fb884bc406e227957、
01690baef29f78ddf27a83ea3281e7b419a26af3a3da94a63edd2a10d940ee6c，
与实际保存的段逐项相同。该只读核对在 V8 执行，不另记 Actions 数学运行。

所以这十八条真实五阶 cochain 最终均位于 155 个纯切向及一次 normal 目标坐标，正阶只用其中 135 个一次 normal 坐标。这个事实可用于下一次较小的原投影计算；它本身不等于已经得到所有更高阶校正。

## 7. 原执行与可复算身份

实际回执：
[43740928483-infinity-fifth-true-shifted-incoming.json](../notes/r150-source-kernel-session-789f/43740928483-infinity-fifth-true-shifted-incoming.json)。

- run：43740928483；
- step：infinity-fifth-true-shifted-incoming；
- execution source：a8a70bc20c64b1f5a90cfbd4b43560cc998e0cbb；
- 数学 23.7528492750007 秒，墙钟 23.86422167799992 秒，exit 0；
- 新源码：../notes/2026-11-15-r150-infinity-fifth-true-shifted-incoming-789f.py；
- 源码 67519 bytes，SHA-256 b8933b780190d3d997a488c2c0424ca3379b3b8e5e13504368da46f21f444906；
- 原临时回执 18558 bytes，SHA-256 7de95d469ed65531253f001581871723235ca9304bd96b7092c816dd30beda75；
- 主线小摘要 22769 bytes，SHA-256 17361fc2f385bbc1ffe8b843d185d0c3acd2998276579d08e5d76e8233eaf036。

本轮 binding 为
ccacc20f5bf3e678c4b3fcab2090e25b84c72abb35440c9b0c8473fa007a8576。

已 verified 的 cochain 临时文件为 171510 bytes，文件 SHA-256
0a7912065c0b03edfa8b1b0aea086729ddcc2ebfbe8fc890e6e06671c0bb01b2；
其完整有理矩阵 SHA 为
91416a4981ee7ec4331f9ab52aaa4dc01e4f8b84e16a11e48c407528b1a6f710。

所有可由脚本和参数重算的矩阵只保留在当前作业临时目录，永久记录只有源码、参数、真实 run 及小回执散列。
