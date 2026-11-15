# R150 补篇：原完整无穷远模31谱、十三形式核与所选子式的剩余28

日期：2026-11-15 UTC。作者：Astra-ISP-789f / root 与 normal_annihilator。AI-assisted，GPT-6 Astra Pro。

状态：原全部 $6188$ 个来源、全部 $4367$ 个输出在自然无穷远参数中的完整有限域计算已经通过。它给出原 full 矩阵的准确模 $31$ 正 Smith 谱和十三个形式自由方向；特征零仅按同一整数子式推得上界，不把有限域谱搬到有理数域。

## 1. 同一原矩阵与完整谱

取 $u=1/s$，保原权齐次化、原十七式及其全部次数至多三的乘子：
$$
A(u)\in R^{4367\times6188},\qquad
R=\mathbb F_{31}[[u]].
$$
N 的线性部分按参数次数十反转，N 的二次部分为常项，六条 Gamma 的二次部分按次数五反转。本轮先将原 primitive 整数方程的全部 $4433$ 个参数系数与冻结 native 模型逐项比较；原固定分母及十七个行尺度均在 $31$ 处为单位。

实际原常秩为 $4340$，函数域秩为 $4354$。完整正 Smith 谱准确为
$$
\boxed{1,1,1,1,3,4,4,4,5,6,7,8,10,11.}
\tag{1.1}
$$
因此
$$
\boxed{\delta_{\mathrm{full},31}=66,\qquad
       \delta_{4353,31}=55,\qquad a_{\max,31}=11.}
\tag{1.2}
$$
原余核自由秩为 $13$。这些数来自自然无穷远的独立原矩阵执行；它们数值上与已有仿射零点谱相同，但本证明没有用两点相同作为任何推理前提。

## 2. 实际4340常单位与自然低次数尾

旧 $3333$ 个预基的 F/B 操作仅正规化最高单项式次数块。自然 $A_0$ 中仍有低次数 pre-pivot 尾；首版要求整个预基主块为单位阵的断言已实际失败，失败记录完整保留，未产生任何新 jet。

修订版实际核对全部预基主分量：对角为一，所有非零非对角项严格向后，单项式次数严格下降。实际共有
$$
1\,711\,875
$$
个此类非零尾，次数下降均为一。正向消元按原输出 pivot 顺序，伴随消元反向使用完整 $4367$ 坐标的预基行，没有只保 $1034$ 个补坐标。

若正向一步为
$$
\alpha_i=x_{p_i},\qquad x\longleftarrow x-\alpha_i\phi_i,
$$
完整伴随为
$$
\lambda\longleftarrow
\lambda+(a_i-\phi_i^T\lambda)e_{p_i}.
$$
首版遗漏的 pre-pivot 尾全部在内。

随后重放旧 full 来源 DAG 的另 $1007$ 个实际单位主元。保留其真实非零主元系数，不假装已经归一。全部 $782976$ 个 forward、$1010703$ 个 backward 及 $1203382$ 个 full 来源消元操作均按原字典重放。此次没有新的大 Gaussian 消元，也没有重新构造旧多项式正常形。

记真实原单位输出和来源为 $I_0,J_0$，均有 $4340$ 个；补输出为 $F_0$，有 $27$ 个；补来源为 $T_0$，有 $1848$ 个。完整原字典身份由执行小回执锁定。

## 3. 二十七个原 dual jets 与全部来源残量

令
$$
W=\iota_{J_0}\bigl(A_0[I_0,J_0]\bigr)^{-1}\pi_{I_0}.
$$
上述来源 DAG 及完整三角伴随实现 $W^T$，不分配新的 $4340$ 阶逆。

初始原 cochain 为
$$
L_0=\iota_{F_0}-W^TA_0^T\iota_{F_0}.
$$
实际核了 $L_0[F_0,:]=I_{27}$ 及全部 $6188\times27$ 个原常数零产品。对 $k\ge1$，取
$$
L_k=-W^T\sum_{a=1}^{\min(10,k)}A_a^TL_{k-a},
$$
并保留完整残量
$$
R_k=A_0^TL_k+
\sum_{a=1}^{\min(10,k)}A_a^TL_{k-a}.
$$
每阶实际核全部 $4340$ 个单位来源上的残量为零，以及全部二十七个高阶自由输出坐标为零。其余全部 $1848$ 个来源行构成 $S_k$；没有再删除剩余行。

形式上
$$
L(u)=\iota_{F_0}
-\iota_{I_0}\bigl(A(u)[I_0,J_0]^T\bigr)^{-1}
 A(u)[F_0,J_0]^T,\qquad
S(u)=A(u)^TL(u)\big|_{T_0}.
$$
所以 $S$ 是原 $A^T$ 在实际常单位消去后的完整 $1848\times27$ Schur 矩阵。

## 4. 全部十四个正指数和十三个真正形式自由方向

本轮计算全部自然系数 $0,\ldots,21$。原泛参数十三核定理使全部 $4355$ 阶整数子式恒零，约化模 $31$ 仍零；同一已付非零 $4354$ 阶子式给相反下界。因此 $S$ 的函数域秩准确为十四。

同一选定方阵 $B$ 的完整模 $31$ 正谱总和 $243$、最大指数 $21$ 已经独立付清。由
$$
\operatorname{tors}\operatorname{coker}A
\hookrightarrow\operatorname{coker}A_I,
\qquad
\operatorname{coker}B\twoheadrightarrow\operatorname{coker}A_I,
$$
原 full 的所有正指数均至多 $21$。因此二十二个实际系数足以要求完整退出；程序不会把未退出方向预填成自由核。

实际每阶退出秩如下：

| 自然阶数 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 退出秩 | 0 | 4 | 0 | 1 | 3 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |

每次仅以实际单位块作 Schur 消去，核所有单位逆的 Taylor 卷积，保全部剩余来源行。十一阶已付清十四个正方向，已知的剩余系数全部为零，得到 (1.1)。

实际十四行列主子式非零；加上函数域秩上界十四，剩余形式 Schur 恒零。连续单位 Schur 的右 graph 组合给出
$$
N(u)\in R^{27\times13},\qquad S(u)N(u)=0,
$$
其十三个自由坐标为单位阵。等价的精确形式表达式为
$$
N=\iota_F-\iota_C\,S[R,C]^{-1}S[R,F].
$$
其中逆式的正则性由实际逐步单位 graph 支付，不是忽略其中可能出现的 $u$ 分母。

令
$$
K_{\mathrm{left}}(u)=L(u)N(u).
$$
则
$$
A(u)^TK_{\mathrm{left}}(u)=0,
$$
且十三个指定原输出坐标为单位阵。另实际生成其常数列于全部 $4367$ 坐标，乘回全部 $6188$ 个原来源，核了
$$
6188\cdot13=80444
$$
个常数坐标为零。完整形式结论使用上述泛秩与单位 graph 证明；没有声称已数值乘回这十三核的所有无限高阶系数。

## 5. 特征零可以和不可以直接得到的界

把实现 (1.2) 的原整数 $4354$ 阶及 $4353$ 阶子式分别取出。其在对应阶数的系数模 $31$ 非零，故同一有理子式在 $u=0$ 的消失阶不更大。因此
$$
\delta_{\mathrm{full},\mathbb Q}\le66,\qquad
\delta_{4353,\mathbb Q}\le55.
$$
结合[原完整无穷远第三连接](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)已经证明的 $43/39$ 下界，
$$
\boxed{43\le\delta_{\mathrm{full},\mathbb Q}\le66,\qquad
39\le\delta_{4353,\mathbb Q}\le55.}
\tag{5.1}
$$
特别地，特征零完整最大正指数满足
$$
a_{\max,\mathbb Q}
=\delta_{\mathrm{full},\mathbb Q}-\delta_{4353,\mathbb Q}
\le27.
$$
这里没有推出它至多十一；个别 Smith 指数不能由有限域的同序号值直接抬升。特征零完整谱仍需真实来源证明或计算。

## 6. 旧两项判据在此固定Koszul族上的准确限制

同一原外支撑矩阵
$$
O=\operatorname{pr}_{J^c}\Phi\in R^{1834\times1632}
$$
已由新的四输入重建实际付清全部有限域正谱
$$
1^2,\ 2^{10},\ 3^3,\ 4^3,\ 5,\ 6,\ 8^2,\ 9,\ 10^2,\ 11,\ 12,\ 13,\ 14,
$$
总和 $149$、最大 $14$；全部 $29$ 个原来源及 $126643$ 个常数产品通过。见[实际 O 小回执](../notes/r150-full-infinity-dual27-session-789f/43731615668-koszul-outside-minimal-original-field-through21.json)和[原扭子注入证明](R150-appendix-koszul-outside-torsion-embedding-and-selected-minor-test.md)。

同一最大子式比较给
$$
\sigma_{O,\mathbb Q}\le149.
$$
因此，无论后续如何精确求出这两块的特征零值，都有
$$
\boxed{\delta_{\mathrm{full},\mathbb Q}
+\sigma_{O,\mathbb Q}\le66+149=215<243.}
\tag{6.1}
$$
所以只使用旧判据中的这两项，不能将同一选定 $D$ 的无穷远阶夹逼到 $243$，也不能据此支付其首项 $31$ 单位。这只关闭这个固定两项判据的封口可能；没有否定 $D$ 的实际首项为单位。

## 7. 剩余28的完整投影分解

下面在任一当前域的离散赋值环 $R$ 中证明精确分解，各域分别使用自己的原始核基。

令 $K=\ker A$、$\Psi=\operatorname{pr}_{J^c}|_K$。原选定 $B=A[I,J]$ 泛可逆，给精确序列
$$
0\longrightarrow\operatorname{coker}\Psi
\longrightarrow\operatorname{coker}B
\longrightarrow\operatorname{coker}A_I
\longrightarrow0.
\tag{7.1}
$$

记饱和像
$$
L^{\mathrm{sat}}
=(\operatorname{im}A\otimes\operatorname{Frac}R)\cap R^{4367}.
$$
取任一原始完整左核基
$$
K_{\mathrm{left}}:R^{13}\longrightarrow R^{4367},
$$
它的转置满射且 $L^{\mathrm{sat}}=\ker K_{\mathrm{left}}^T$。设
$$
G_I=K_{\mathrm{left}}[I^c,:]\in R^{13\times13},\qquad
\lambda_I=v_u\det G_I.
$$
$I^c$ 必须是同一选定 $B$ 的原补输出十三项，不能换成本轮新单位块的自由字典。$\lambda_I$ 不依赖左核原始基的单位变换。

投影到 $I$ 在饱和像上单射，并有
$$
R^I/\pi_I L^{\mathrm{sat}}
\simeq R^{13}/\operatorname{im}G_I^T.
$$
这是因为 $K_{\mathrm{left}}^T$ 满射，而 $I^c$ 部分恰给 $G_I^T$。又
$L^{\mathrm{sat}}/\operatorname{im}A$ 的长度为 $\delta_{\mathrm{full}}$，故
$$
\operatorname{length}\operatorname{coker}A_I
=\delta_{\mathrm{full}}+\lambda_I.
\tag{7.2}
$$

原 $\Phi(0)$ 满列秩 $1632$，所以 $\operatorname{im}\Phi$ 是原始直和因子，
$K/\operatorname{im}\Phi$ 无扭、秩为 $202$。由
$$
0\longrightarrow K/\operatorname{im}\Phi
\longrightarrow\operatorname{coker}O
\longrightarrow\operatorname{coker}\Psi
\longrightarrow0
$$
以及
$\operatorname{coker}O/\operatorname{tors}$ 的自由秩同为 $202$，定义
$$
\delta_{\mathrm{high}}
=\operatorname{length}\operatorname{coker}
\left(K/\operatorname{im}\Phi
\longrightarrow
\operatorname{coker}O/\operatorname{tors}\right).
$$
这个映射单射且泛同构：其像与扭子部分交为零，且两边自由秩相同。因此
$$
\operatorname{length}\operatorname{coker}\Psi
=\sigma_O+\delta_{\mathrm{high}}.
\tag{7.3}
$$

合并 (7.1)–(7.3) 得完整、没有遗漏自由投影的恒等式
$$
\boxed{v_u\det B
=\delta_{\mathrm{full}}+\lambda_I+\sigma_O+\delta_{\mathrm{high}}.}
\tag{7.4}
$$
有限域实绩现在给出
$$
\boxed{\lambda_{I,31}+\delta_{\mathrm{high},31}
=243-66-149=28.}
\tag{7.5}
$$
两项均非负。下一项具体计算是用同一 $I^c$ 计算真实 $13\times13$ 的 $G_I$，再决定剩余的 $202$ 维自由商贡献。到本稿发表时，两项尚未分别求值。

(7.5) 不能直接搬到特征零：原始形式核基的模 $31$ 运输还须另付，不能只因函数域秩相同就默认平坦。特征零中恒等式 (7.4) 本身仍成立。

## 8. 实际运行与可复算身份

本次成功 run 为 43731615668，步骤 full-infinity-original-dual27-v2-through21，execution source 为
f44e943989d93799d66e80d99d98c8fc4557c055。

- 编译 4.526625665 秒，数学 9.075420298 秒，墙钟 13.702745871 秒，退出码 0。
- 原临时小回执 21358 B，SHA256 为 540fd2d44e7d49f9d4284d8966e9994397320f145e353c1560c7807f76caf9b4。
- 语义 binding 为 3e51cbe960ac668c9addb12be36856d2aaf13686f5acc15571317ccf3dd7d2ad。
- [native v2](../notes/2026-11-15-r150-full-infinity-natural-dual-schur-v2-789f.cpp)：21017 B，SHA256 82ce435444ea112e78d842a7975df4a6b6103f6ea0bf03efc73f58631985d6f9。
- [runner v2](../notes/2026-11-15-r150-full-infinity-natural-dual-schur-v2-runner-789f.py)：26512 B，SHA256 8efdcae153794c6dcf61e15f3744232feaeb223b9ba98c30309a9731864c34e0。

[完整实际小回执](../notes/r150-full-infinity-dual27-session-789f/43731615668-full-infinity-original-dual27-v2-through21.json)
保全部原系数、预基三角尾、常单位、自然 residual、Schur、十三 mapper 及临时数组 SHA；[接口说明](../notes/2026-11-15-r150-full-infinity-natural-dual-schur-v2-interface-789f.md)
保六件历史输入和精确 CLI。所有可重算大数组只在当前临时 job 存在，没有上传 Git 或 Release。

本篇没有完成原 $h_0$ 九目标的全局 $\mathbb Q[s]$ 成员性，没有支付固定 $D$ 的首项单位，也没有改变普通复可分无限维 Hilbert ISP 的完成标准。
