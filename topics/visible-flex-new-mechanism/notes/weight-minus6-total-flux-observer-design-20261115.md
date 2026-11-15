# R342：从四个已发表 mixed 原根观察权负六纯核的真实总通量

日期：2026-11-15。**观察设计和新消费源码；新人工与新科学尚未执行。**

本稿固定一个新的观察任务：从 R144 已保存的四个完整相位 $-2$ 原根，求一个明确 pure 恒零成本在一个预先指定的实 profile 族上的总通量。只消费原表达式，不重新编译 forcing、第三模板、原响应列、平移链或 pure/self 矩阵；不重新支付旧秩或旧非成员结论。

新程序的输出目标是**有限 profile 族上的精确多项式以及可能的非零见证**。它不是一般泛函的忠实坐标系。若该多项式为零，结论仅为本预设族未检出，不能宣布一般总通量恒零。

## 1. 为什么这个观察仍是新问题

[R338](../results/R338-weight-minus-six-pure-response-total-flux-and-exact-tail-coordinate.md) 已从完整原尾和 20 个原响应标签证明
$$
\Omega_u(V):=\int_1^4 u'''(x)V(u^2,0)(x)\,dx=0
\quad(V\in\mathcal R_{-6}\cap\ker\pi)
\tag{1}
$$
对每个实紧光滑 $u$ 成立。这里 $\pi$ 是原 canonical 相位 $-4$ 投影，$\mathcal R$ 是完整真实响应空间。

R338 没有把式 (1) 扩到 $\mathcal U_{-6}\cap\ker\pi$。R144 已证明 $N^7G$ 不在完整响应空间；本任务不重复该非成员证明，而是判断一个指定的 pure 零代表是否被新的真实总通量检测到。

若本次得到 $\Omega_u(A)\ne0$，就严格得到式 (1) 的响应消去泛函在实际 $\mathcal U_{-6}$ 上非零。这一结论给出原 $L_f$ 总通量必要条件的一个完整成本方向。尚未证明该方向就是某个指定几何的最终 period，不能自动升级为该几何整体不可行；也不能由 whole pure/self 成本是否为零代替此观察。

## 2. 从既有 pure 恒等式得到准确四根组合

沿用 [R138](../results/R138-general-pure-G-identity-and-affine-orbit-kernel.md) 的真实恒等式
$$
\pi G=\frac1{128}\pi\mathfrak B_Q([L,Q]),
\qquad
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\
V=\Phi_{p_1},\ T=\Phi_{t_1},\ Q=\Phi_{p_2}.
\tag{2}
$$
括号保留完整外槽；不把它替成仅对角表达式。

原真实平移导子满足
$$
\begin{aligned}
NQ&=2V-T/2,&N^2Q&=2L-2U,\\
N^3Q&=-3(R+S),&N^4Q&=-6P,&N^5Q&=0,\\
NL&=(S-R)/2,&N^2L&=0.
\end{aligned}
\tag{3}
$$
这些是原 E8 算子的同锚平移关系。对 $\mathfrak B_Q([L,Q])$ 的三个位置作 Leibniz 展开，只剩下面五种分配。$R_j$ 始终是 R144 的**原 20 列编号**。

| $(N\text{ 落外 }Q,N\text{ 落 }L,N\text{ 落内 }Q)$ | 除以 630 的完整响应 |
|---|---|
| $(3,0,4)$ | $R_{10}+R_{14}$ |
| $(4,0,3)$ | $R_2+R_3$ |
| $(2,1,4)$ | $R_1-R_0-R_{19}+R_{18}$ |
| $(3,1,3)$ | $-2R_{12}-2R_{16}$ |
| $(4,1,2)$ | $R_3-R_2+R_7-R_6$ |

因此
$$
\begin{aligned}
N^7\mathfrak B_Q([L,Q])=630\{&
-R_0+R_1+2R_3-R_6+R_7+R_{10}\\
&-2R_{12}+R_{14}-2R_{16}+R_{18}-R_{19}\}.
\end{aligned}
\tag{4}
$$
没有调用程序生成式 (4)。

[R207](../results/R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 的原 pure 表，以
$$
\rho_0=\pi R_0,\quad \rho_2=\pi R_2,\quad\rho_3=\pi R_3
$$
为基。式 (4) 中括号的既有三坐标准确相加为 $(-2,-4,2)$，故
$$
\boxed{\pi N^7G=\frac{315}{32}(-\rho_0-2\rho_2+\rho_3).}
\tag{5}
$$
本轮不会重新评价任何相位 $-4$ 根来检验已经由式 (2)–(4) 和旧表推出的式 (5)。

固定完整成本
$$
\boxed{
A=N^7G+\frac{315}{32}R_0+\frac{315}{16}R_2-\frac{315}{32}R_3
\in\mathcal U_{-6}\cap\ker\pi.
}
\tag{6}
$$
R338 的 pure 尾坐标为 $\ell(a\rho_0+b\rho_2+d\rho_3)=a+b+3d$；式 (5) 的尾坐标为零。此事实不许可删掉四个 mixed 原根的真实 primitive 常数；程序仍直接保留全部原常数。

需要的原响应身份只有
$$
R_0=\mathfrak B_L([P,R]),\qquad
R_2=\mathfrak B_P([L,R]),\qquad
R_3=\mathfrak B_P([L,S]).
\tag{7}
$$
不把原列号换成后来 13 条 pure 核列号或压缩后的列号。

## 3. 为什么只读相位 $-2$，以及因子 $-4$

对真实成本取 $f=u,g=0,\phi=u\cos\theta$。完整 ruling 的形式是
$$
V(u^2,u\cos\theta)=A_0+B_0\cos^2\theta+C_0\cos^4\theta.
$$
原端点 $D=0$ 给 $A_0+B_0+C_0=0$。相位 $-2$ 的系数准确为
$$
M_{-2}(u,u)=\frac14(B_0+C_0)=-\frac14V(u^2,0).
$$
因此新观察为
$$
\boxed{
\Omega_u(A)=-4\int_1^4u'''(x)
\left(M^{N^7G}_{-2}
+\frac{315}{32}M^{R_0}_{-2}
+\frac{315}{16}M^{R_2}_{-2}
-\frac{315}{32}M^{R_3}_{-2}\right)(u,u)(x)\,dx.
}
\tag{8}
$$
四个根都来自同一个旧原导出；不从 pure 根猜 mixed，不重新求原 phase forcing。

## 4. 预先固定的有限 profile 族

置 $t=x-2$，固定
$$
u_\lambda(x)=
\begin{cases}
t^8(1-t)^8\{1+\lambda(2t+3t^2+5t^3)\},&2\le x\le3,\\
0,&x\in[1,4]\setminus[2,3].
\end{cases}
\tag{9}
$$
支撑、原右锚 $4$、扰动多项式及下面六个见证点都在运行前固定。不会根据本次结果自动改 profile、提高次数、扩大搜索族或观察另一个权。

式 (9) 的零延拓是 $C^7$，**不是 $C^\infty$**。全部端点 jets 到七阶为零。旧原导出的最大输入 jet 为四阶，新消费器还逐可达 atom 检查此范围；因此式 (8) 在固定区间上的实际有限 DAG 是 $C^4$ 连续泛函。每个同锚有限积分在相应一致范数下连续，所有乘积与最后外积分也连续。

取光滑内截断 $\chi_\epsilon$，使其在 $[2+\epsilon,3-\epsilon]$ 上等于 1、在更小端邻域为零。由于 $u_\lambda$ 在两端有八阶消失，
$$
\chi_\epsilon u_\lambda\longrightarrow u_\lambda\quad\text{于 }C^4([1,4]).
$$
故若式 (8) 在某个式 (9) 的 profile 上非零，充分小正 $\epsilon$ 给一个真实 $C^\infty_c((2,3))$ profile，保持同一总通量非零。程序不会声称有限多项式零延拓本身已经光滑；也不会声称已经给出该光滑截断的显式数值宽度。

完整成本对输入为四次，外面再乘一个 $u'''$，所以
$$
\mathscr O(\lambda)=\Omega_{u_\lambda}(A)\in\mathbb Q[\lambda],
\qquad\deg\mathscr O\le5.
\tag{10}
$$
程序在 $\mathbb Q[t,\lambda]$ 中准确求出整条多项式，输出每个非零系数。若不恒零，就在预设顺序
$$
\lambda=0,1,2,3,4,5
$$
中选第一个非零值。非零五次以下多项式不可能在六个不同点全零。

若 $\mathscr O=0$，程序只报告“该预设族为零，普遍泛函未判”。即使保存了六个零值，也不能把这个有限族叫作一般 profile 空间的忠实观察。

## 5. 原右锚不能无条件换成支撑端

旧原导出的积分约定是 signed
$$
I(F)(x)=\int_4^x F(\xi)\,d\xi=-J(F)(x).
\tag{11}
$$
本程序对实际可达的每个原 atom 递归计算 profile 次数。原 jet 次数为 1，乘积相加，$x$ 次数为 0，积分保留被积函数的 profile 次数。只有每个实际积分的被积函数次数严格正，才允许以下归纳：

1. 所有输入 jets 在 $[3,4]$ 恒零。
2. 一个已验证的正 profile 次数 primitive 在 $[3,4]$ 也恒零，因为其所有依赖 atom 已在该区间为零。
3. 每个实际积分的被积函数至少有一个这样的正次数因子，故在 $[3,4]$ 恒零。

于是仅在支撑区间 $x=2+t$ 上，原式 (11)准确等于
$$
I(F)(2+t)=\int_1^tF(2+s)\,ds.
\tag{12}
$$
对每个 $\lambda$ 系数分别保留式 (12) 的右端常数。嵌套积分每一层都保自己的常数。

若原 DAG 中出现无 profile 因子的 $I(1)$ 或类似项，程序会明确拒绝此次未支付的移锚，不能把其原锚 4 静默换成 3。没有凭单个最终 root 的总 profile 次数四就跳过内部检查。

左侧 $[1,2]$ 的真实多项式尾没有被宣布为零。外因子 $u'''$ 在该区间为零，所以式 (8) 的最终外积分可以限到支撑；支撑内各层 primitive 的真实常数全部仍在。

## 6. 唯一旧输入与完整来源

旧公开 run **43655713308**，source
**d21c87a4d9341369a3dee35598ed88fb666cb99d**，lane
**g_translation_successor**。目录为
**notes/actions-43655713308-1-g_translation_successor**。

| 旧文件 | bytes | SHA-256 |
|---|---:|---|
| G-seventh-translation.json | 26745 | f5e514164cede76ba91786833d455b4638a45a3ee82cd2b7cadbcd76ee18ff15 |
| receipt.json | 35234 | d1a5b9d8aa03553dfcf45731cbbbbb7861fbcbb496e90fb960e723e1597c3389 |
| G-seventh-translation-original-expressions.json.gz | 15427 | 936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664 |
| 上项原文，仅 runner 内存解压 | 80081 | cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb |

目标相位 $-2$ 原根 hash 为
**67e55d68ca5498a698438f389ffb28346aaed3da329cd024a5332183846ed09c**。

只读四个 root：`target_-2`、`column_000_-2`、`column_002_-2`、`column_003_-2`。准确拼写和四个有理权在 request/source 中固定。消费器核原列标签、原 root 链接、原导出 schema、终端 receipt 的 gzip/raw 双 hash、旧 run/source 和完成状态。

全部原文由 raw SHA 绑定。旧 root hash 标签在这层绑定下消费；程序**不重构原 Ring.digest**，不冒称重新验证全部旧 root 编译。只遍历四个根实际可达的原 DAG，未选根不求值。

冻结 producer 和 serializer 源码仅读文本身份，不 import：

| 原脚本 | bytes | SHA-256 |
|---|---:|---|
| literature_G_translation_successor.py | 39670 | a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406 |
| literature_local_fourth_quotient.py | 38857 | 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0 |

新入口 [literature_weight_minus6_total_flux_observer.py](../scripts/literature_weight_minus6_total_flux_observer.py) 只用 Python 标准库。request 同时绑定该新脚本的最终 bytes/SHA。

## 7. 一次新公开任务的执行范围

主入口读取 [request-total-flux-observation.json](../computations/request-total-flux-observation.json)，CLI 只有 --request PATH 与 --out PATH。输出路径是该 run 的临时目录，不是仓库内新数据路径。

程序先执行十项**新增**接口人工：精确双变量乘法、单位宽物理导数、逐参数 signed 原函数常数、两个原颜色映成同实 profile、嵌套常数、右端值、无 profile 积分拒绝、$-4$ 观察规范、四根组合及零族的结论边界。它们只用小人工字典，不读研究输入。首次执行只能在公开 Actions；本稿状态是全部未执行，不写 passed。

新科学共享上限为：

| 项目 | 上限 |
|---|---:|
| 新观察 wall | 120 秒 |
| RSS | 512 MiB |
| 精确有理乘积计数 | 15000000 |
| 有理分子/分母位数 | 8192 bits |
| $t$ 次数 | 160 |
| $\lambda$ 次数 | 5 |
| 临时 JSON | 95000 bytes |
| 主要人类科学输出 | 35000 bytes |

小人工单独记录自己的时间/乘积统计；不会借它运行任何真实原根。旧 forcing、N 链、old toy、pure/self/rank/member 计算次数全部为零。

四个 root 各只求值一次。除直接对组合求一个外积分，还把四个独立积分按固定权重相加，用同次结果核准确重组；这不重复原 root 求值。记录实际可达 atoms、单项式、最高 jet、已验证积分数和实际预算。

任何来源、边界、容量或新人工失败都输出 error，不把旧完成状态改成新成功。研究值尚未知；不为追非零增加原预算或自动换族。

## 8. 输出、保存规则和下一结论

主要 stdout 输出整条 $\mathscr O(\lambda)$、非零见证（若有）、该见证上的四个未加权新观察值、四个组合权、原 source/run/raw SHA 和本次资源统计。临时 JSON 留全部新系数与来源以供本次 publisher 计算大小/hash。

遵守当前根规则 15：**不把可重算原 payload、新 JSON、机器证书或 Actions 输出提交到仓库或 Release，也不建 artifact 保存它们**。源码、固定 request、run 与输出 SHA、人的数学结果才进入正式记录。旧已存在 gzip 只作为本次必要原输入消费，runner 内解压不等于重新保存一份。

两个可能结果的准确范围为：

- 若非零：存在真实紧光滑 $u$ 使指定 $A\in\mathcal U_{-6}\cap\ker\pi$ 的 $\Omega_u(A)\ne0$。R338 所限总通量确能检测一个已存在的完整成本方向；它不能通过添加 $\mathcal R_{-6}\cap\ker\pi$ 响应消去。
- 若该族全零：只得到式 (9) 的精确限制为零。一般 $\mathcal U_{-6}$ 上的总通量、其它 profile 族及完整 period 继续未判。

本任务不支付全部 $\ker L_f$ 的同一 $w$、$V_e$、其它内部退化点、平台/端点条件或原主课题。

窄独立纸核：literature 已逐项核式 (4) 的五种 multinomial 分配与括号方向；未据此宣称执行过新程序或重审全部旧表。
