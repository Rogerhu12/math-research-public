# R98 字符在真实第四阶横向上的四列查询

日期：2026-11-14。独立下一步设计与纸面引理。只运行过人工小型代数 toy；本稿没有新的研究 profile、几何或完整目标计算。研究入口为 [literature_fourth_character_transverse_probe.py](../scripts/literature_fourth_character_transverse_probe.py)。

## 1. 已证明的 P1 门不自动是 P0 门

[R98](../results/R98-weight-zero-separation-of-all-positive-state-P1.md) 在真实有限函数空间

$$V=\mathcal R_*+\operatorname{span}\{b_{H,d}\}$$

上给出 $\Lambda(\mathcal R_*)=0$、$\Lambda(b_{H,d})=1$。这里 $\mathcal R_*$ 只由 reciprocal 二阶算子的七维空间

$$E_7=\{p_1+4t_1=0\}$$

作用于完整第三空间 $W$ 生成。它没有覆盖 [R83](../results/R83-true-fourth-transfer-and-zero-lower-history-variations.md) 允许的任意八矩 $P$。

取缺失方向 $P=\Phi_{t_1}$。R83 的真实 $M=T=0$ 控制族给整个相位函数的切向

$$\begin{aligned}
K_{P,T}(F,\phi)
={}&2T(PD;D)-4T(\phi;\phi,PD)
+4P(\phi,T(\phi;D)),\\
&D=F-\phi^2.
\end{aligned}\tag{1}$$

这正是既有完整两模式响应 $\mathcal B_P(T)$。$P$ 的权为零，所以权零查询只需 $W_0$ 的四个已绑定原模板：

| 新列 | 第三方向 | v2 原序号 | 是否已有准确零证明 |
|---:|---|---:|---|
| 0 | $\tau_{p_0,p_2}$ | 1 | 完整相位 Jacobi |
| 1 | $\tau_{p_1,t_1}$ | 12 | 尚无 |
| 2 | $\tau_{p_2,s_1}$ | 16 | 完整相位 Jacobi |
| 3 | $T_k^{\rm shape}$ | 109 | 尚无 |

这里 $\tau_{Q,R}(a;b,c)=Q(a,R(b,c))-R(a,Q(b,c))$，$T_k^{\rm shape}$ 的方向及全部系数固定为旧原模板，不另行归一。四列中的两个已知零是本次原式数值核的定向检查，而不是要再次发现的大空间关系。

## 2. 完整相位 Jacobi，而非只对角 Jacobi

对任意三个对称双线性算子 $P,Q,R$，由 (1) 逐项展开可得

$$\boxed{\mathcal B_P(\tau_{Q,R})+
\mathcal B_Q(\tau_{R,P})+
\mathcal B_R(\tau_{P,Q})=0.}\tag{2}$$

这是对整个 $(F,\phi)$ 的准确身份。第一组项为

$$2\sum_{\rm cyc}\{Q(PD,RD)-R(PD,QD)\},$$

由双线性对称性两两消失。其余两组分别为

$$-4\sum_{\rm cyc}\{Q(\phi,R(\phi,PD))-R(\phi,Q(\phi,PD))\}$$

和

$$4\sum_{\rm cyc}P(\phi,Q(\phi,RD)-R(\phi,QD)),$$

经循环重排准确相消。证明没有假设算子结合、交换或忽略混合相位。

沿用 R98 权零表的 $C_j$，(2) 特别给

$$\begin{aligned}
\mathcal B_{t_1}(\tau_{p_0,p_2})&=C_9-C_1,\\
\mathcal B_{t_1}(\tau_{p_2,s_1})&=C_3-C_{13}.
\end{aligned}\tag{3}$$

两个右侧都属于真实 $\mathcal R_*$。所以任何按原查询公式延拓的 $\Lambda$ 在这两列上也准确为零；后面的模零只是独立执行检查，不是此结论的唯一依据。

## 3. 明确定义扩展，不预设新列属于 V

消费 R98 已发布的权零文件

`notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p0.json`，

其原始长度为 56173 B，SHA256 为

`1146e6789d2f842ecc255930e2394bec5073029b13dcff4cc6f1aa445d07a78d`。

令 $A$ 为 R98 保留的 14 个原列在其 14 个 pivot 查询上的准确有理矩阵，$a$ 为第 15 个查询对应的行。这里查询仍是原来同一对实有理 profiles 的 $-4/-2$ 模式实部或虚部。原证书证明 $A$ 可逆。定义

$$\lambda_0(X)=\operatorname{ev}_{23}(X)
-aA^{-1}\operatorname{ev}_{\rm pivot}(X),\qquad
\kappa=\lambda_0(b_0)\ne0.\tag{4}$$

对任何足够正则、拥有同一查询定义的有限权表达式，现在**另行定义**

$$\boxed{\widetilde\Lambda(X)=\lambda_0(\Pi_0X)/\kappa.}\tag{5}$$

(5) 在原 $V$ 上与 R98 的 $\Lambda$ 一致。它也可用于新的第四切向，但不意味着新切向已属于 $V$，更不意味着 (2) 以外的全部新方向已被旧门排除。四个新响应原式都直接核权零，故本次不需从它们再编译其他权。

所有有理泛函系数以 (4) 定义。报告中的模 $p$ 系数仅为其约化，绝不拿打印的模数代表当作实系数，也不从余数大小读取实数符号。

## 4. 原式评价与输入身份

代码先核旧文件的原始长度/SHA、run `43638896281`、完整源码身份、权零完成状态、16 原列到 14 真上界的两条已验证关系。然后只从旧报告中的 15×15 模增广矩阵重核旧泛函消 14 列、$\kappa\ne0$ 及 Schur 行列式关系。它不重新评价旧列、旧目标，不重新消元旧空间，也不重新运行其 14/15 阶证书。

研究编译只恢复四个第三原模板：前三个直接由 $\Phi_8$ 括号生成；最后一个从完整 R56 外槽/内槽 local root 及其真实 R73/R79 分解中提取 `h_shape_obstruction` 的 $k$ 系数。该单 root 的重构检查保留；没有编译旧常态第四目标。每个模板逐一比对旧 SHA、权零和真实内槽对称。

随后将四个原模板分别代入完整 (1)，并用原来的固定 pair

$$f=[t(1-t)]^8,\qquad
g=f(1+2t+3t^2+5t^3),\quad t=\xi-2\in[0,1]$$

评价原来 15 个查询。全部原语均为真实共同右锚积分；使用原式 polynomial evaluator，不以 word 正规形替代查询。两模式共用同一 pair、同一模板、同一 $P=t_1$。原 pair 的零延拓为 $C^7$，本身没有施加三矩圆条件，报告明确保留此事实。

素数固定为 $p=2147483647$。所有新原式有理分母继续由 evaluator 核可逆。输出每列的两模式 polynomial hash、15 个值、未归一与归一字符余数、所用分母/次数预算和完整源码身份。

只要某个新余数非零，就证明 (5) 对该新原式的准确有理值非零。它不提供该值的实数正负。未知列若余数零，本次只报告未分辨，不能宣称准确为零。若已知的两列出现非零，立即作为实现检查失败退出。

## 5. 与真实第四族的联系及保留成本

R83 对任意已真实实现的第三方向 $T$ 给

$$V_{Z(t,\lambda)}=E(t)+2\{V_{L(\lambda)}-V_{L(0)}\}
+\lambda t\,\mathcal B_P(T),\qquad E(-t)=E(t).\tag{6}$$

且 $M_Z=T_Z=0$ 精确成立。把同一个实际基准中的 $Z(0,\lambda)$ 换成 $Z(t,\lambda)$ 后，完整四块第四常项的切向是 $4\lambda\mathcal B_P(T)$；它不改变低阶 $M,T$ 或已固定的 $P_1$。因此一旦本次非零成立，就可证明某个真实第四切向对扩展字符有非零响应，参数 $t$ 的两侧给基准附近的有符号变化。

但 (6) 的基准

$$4V_{A(0)}+2V_{L(\lambda)}+2V_{L(0)}$$

和 $E(t)-E(0)$ 仍然存在。没有把函数差当作可用倒行实现的负路径；第四倒行成本仍同号。即使四列中有非零，也不支付完整 $P_0+NP_1$、实数负基准、第四 ruling、有限等距族、嵌入、reach 或宏观幅度。

若要转成合法 $C^\infty$ 三矩圆，还须另用充分正则连续性、光滑化及 R86 的左补偿，并保持所有旧查询；当前 consumer 不宣称已选定这样的具体圆。非零算子方向本身与这些后续存在步骤必须区分。

## 6. 预算、toy 与唯一研究入口

默认预算为 120 秒、RSS 软轮询 768 MiB、4 个新列、15 个已绑定查询、100000 B 输出上限；polynomial 次数上限 256、操作上限 10000000。编译 DAG 上限 300000，profile atoms 与单 expression terms 各 100000。失败或资源退出保留已完成列及输入身份，不当数学阴性。源码中研究执行门同时要求 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。

实际研究 CLI：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_fourth_character_transverse_probe.py \
  --max-seconds 120 \
  --memory-mib 768 \
  --output topics/visible-flex-new-mechanism/notes/fourth-character-transverse-probe.json
```

已运行的本地人工 toy 只有：三个人工对称算子 $fg,f'g',I(fg)$ 的完整两模式 Jacobi；三行小矩阵的 Cramer 扩展零/非零；没有研究 profiles、几何或研究 root 编译。其原始报告为 [literature-fourth-character-transverse-development-toy-20261114.json](literature-fourth-character-transverse-development-toy-20261114.json)。公开部署可同 lane 先用 `--toy-only` 再执行上面的唯一实际目标。
