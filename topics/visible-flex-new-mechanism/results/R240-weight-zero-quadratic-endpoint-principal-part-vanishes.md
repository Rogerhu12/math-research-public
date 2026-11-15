# R240：同一权零 pure 零代表的二次平端主部原式消去

日期：2026-11-15。本结论来自本仓库公开 Actions run **43701766182**，不是由 job 的 success 状态推断数学结果。本文完整消费了实际 stdout 中的新人工、唯一研究目标、输入原式身份和 metadata-only receipt。

数学责任范围：七个必要旧原根的恢复、一个新的二次端层提取和精确主部相消均只在公开 Actions 执行；本文在本地只读取已经发布的日志、核对来源与作纸面推论。没有本地研究运算，没有重跑 R234 的十七个一次层或旧 pure 查询。

## 1. 同一个代表与本次结论

沿用 [R234](R234-weight-zero-first-endpoint-layer-cancelled-by-a-zero-pure-response.md) 的原列编号和同一个代表：

$$
H_{\mathrm E}
=C_2-\frac18R_0-\frac1{64}R_1
+\frac{13}{32}R_2+\frac1{48}R_3
+\frac5{64}R_4-\frac1{32}R_{10}.
\tag{1}
$$

其中 $C_2$ 是 [R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md) 的真权零静态原系数，$R_i$ 是 R126 的旧列。这里的下标不是另建的新响应编号。

R234 已经原式支付

$$
\pi H_{\mathrm E}=0,\qquad
\lambda_+(H_{\mathrm E})=1,\qquad
\mathfrak T^\uparrow_{0,-2}(H_{\mathrm E})=0.
\tag{2}
$$

本文继承式 (2)，没有重复计算。$\pi$ 是 whole universal pure 投影；$\lambda_+$ 是 R196 的真实正字符。$\mathfrak T^\uparrow_{0,-2}$ 则只是在**真权零、canonical mixed 模式 $-2$、首个 $f$ 上升且局部 $g=0$ 的左平端**上的一次层。

本次唯一新增的完整结论是

$$
\boxed{
\mathfrak B^\uparrow_{0,-2}(H_{\mathrm E})
=\operatorname{pp}_{<0}\!\left(t^4B_{H_{\mathrm E}}\right)
=0.
}
\tag{3}
$$

$\mathfrak B$ 是 [R236](R236-quadratic-endpoint-principal-part-criterion.md) 的二次主部观测。式 (3) 对下文全部允许的 $c>0$、光滑正振幅及真实同右锚尾函数成立。实际更强地显示：**所有可能进入主部的原式系数在原 DAG 层已经逐项相消**，没有留下需要 quadratic tail word 归约的系数。

式 (3) 不声称原平台条件已经满足。准确的局部推论是：

> 对本文指定的每个真实左端 germ，若 $H_{\mathrm E}$ 的原平台多项式另满足 $P_2''=0$，则其零端通量逆解可光滑延拓到该端点。

这付清的是这个代表、这个端口的一次与二次 germ 门；不是完整 $L_f$ 成员关系，不是整个 period，也不是 joint ruling。

## 2. 真实 germ、尾函数与平台的区分

采用 R225、[R230](R230-first-flat-end-layer-as-an-exact-cubic-tail-operator.md)、R236 的物理材料坐标

$$
t=x-a_*,\qquad
p=f'=\epsilon_p e^{-c/t}a(t),\qquad
c>0,\quad \epsilon_p\in\{1,-1\},\quad
a\in C^\infty,\quad a>0,
\tag{4}
$$

在 $t>0$ 取 $f(t)=\int_0^t p$、$g=0$。首上升取 $\epsilon_p=1$；允许符号只使用相同局部计算，不自动给其他端口或旋转后新圆的结论。真实查询点始终为 $x=a_*+t$，没有把 $a_*$ 置零。

记

$$
\mathscr A=\bigcup_{N\ge0}t^{-N}C^\infty,\qquad
b=\frac{a'}a,\qquad
\lambda=\frac{p'}p=\frac{c}{t^2}+b.
\tag{5}
$$

由已经支付的一次层消去，原目标在这个 germ 可写为

$$
G_{H_{\mathrm E}}=P_2+p^2B_{H_{\mathrm E}}+p^3C,
\qquad B_{H_{\mathrm E}},C\in\mathscr A.
\tag{6}
$$

$P_2$ 是从真实左零平台延入的二次以下多项式，必须与原目标一致。扣去它的二次部分来研究剩余 germ，不等于已经证明原目标满足平台条件。

本次计算在所有原积分节点保持

$$
\mathcal I(E)(x)=\int_r^x E(y)\,dy
=\mathcal I(E)(a_*)+\int_{a_*}^xE(y)\,dy.
\tag{7}
$$

所以局部左增量的符号是正号。每一个 $\mathcal I(E)(a_*)$ 都仍是完整原式在同一个右锚下的真实值。局部 $q=\bar q=f$ 只应用于当前 germ；右侧两个颜色的 profile、嵌套 primitive、shuffle 和端点关系都保留。没有把尾值当成可以独立指定的常数。

当某项局部次数超过二时，其增量不再影响本次观测，但对应原节点的完整锚值仍保留在局部次数零。这个区别保证没有因只求二次层而删掉真实历史。

## 3. 为什么有限截断已覆盖完整主部

实际先扫描式 (1) 的完整可达原 DAG，包括所有嵌套 primitive 的子表达式，得到：

| 原式项目 | 实际值 |
|---|---:|
| 原目标项数 | 2694 |
| 最大可达 profile jet 阶数 $J$ | 4 |
| 报告记录的最大 primitive 深度（观测字段） | 2 |
| 原外部 $x$ 最大幂次 | 9 |
| 可达原 atoms | 2135 |
| 可达原 monomials | 4819 |
| 各原 monomial 的真实 profile 次数 | 全部为 4 |

因此本次不是 $J\le2$ 时由极点界直接给零的分支。完整截断界为

$$
D=2(J-1)=6,\qquad
\operatorname{val}\!\left(p^{-d}\,\text{局部次数 }d\text{ 项}\right)\ge-dD.
\tag{8}
$$

对 $d=0,1,2$ 分别保留到

$$
U_d=-5+(2-d)D,\qquad
(U_0,U_1,U_2)=(7,1,-5).
\tag{9}
$$

这里 $U_2=-5$ 恰覆盖 $t^4B$ 的全部严格负幂。二次系数的保守最低幂为 $-12$，故可能的主部只有

$$
t^{-8},t^{-7},\ldots,t^{-1}.
\tag{10}
$$

截断闭性不是事后观察。若一个局部次数 $d$ 的遗漏项从 $t^{U_d+1}$ 开始，乘上局部次数 $e$、最低幂至少 $-eD$ 的项后，最低幂仍严格高于

$$
U_{d+e}=U_d-eD.
\tag{11}
$$

正局部次数的真实左增量积分还把最低幂提高二；次数零的多项式左积分提高一。因此所有被省略项在之后的乘法、积分和最终次数二提取中都不能返回式 (10)。

令 $b_j=[t^j](a'/a)$。完整会进入主部的振幅参数只需

$$
0\le j\le K=4J-11=5.
\tag{12}
$$

实际保留了 $b_0,\ldots,b_5$，没有预先设定任何 $a(0)$ 或尾数值。$c$ 在有理 Laurent 系数域中保持自由且只允许 $c>0$；没有暗设宽度为一。有限 Taylor 截断之所以授予任意光滑振幅的结论，来自式 (8)–(12) 对余项的封闭性，而不是仅在几个振幅样本上的验证。

若把某一正次数 $d$ 的左积分写成 $p^dS$，递推直接来自

$$
S'+d\lambda S=R,
$$

其系数式为

$$
S_n=\frac{R_{n-2}-(n-1)S_{n-1}}{dc}
-\frac1c\sum_{j\ge0}b_jS_{n-2-j}.
\tag{13}
$$

式 (13) 连同每个节点的完整原锚值准确实现式 (7)，而非把原 $\int_r^x$ 偷换成同号的 $\int_x^r$。

## 4. 实际原式相消及其证明强度

公开实际的最终状态是：

| 项目 | 实际输出 |
|---|---|
| completion | complete |
| complete_quadratic_gate | true |
| outcome | universal_quadratic_principal_part_zero |
| 原主部系数数目 | 0 |
| 新 quadratic tail 转换数目 | 0 |
| 新 quadratic word primitive 调用 | 0 |
| 最终主部完整行数 | 0 |
| 最终完整行向量 | 空向量 |

原主部系数、quadratic 转换记录和最终行向量均为空，三者的规范序列 SHA256 相同：

$$
\texttt{4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945}.
\tag{14}
$$

SHA 只绑定输出，数学依据是：按第 3 节已证明完备的截断计算，所有原式系数已经准确为零。这里没有使用“非完备 NF 的非零就代表非成员”，也没有依赖 word 独立性来证明这个零。事实上本次没有任何非零系数需要送入二次 word 映射。

结合式 (2)、(6) 和 (14)，得到式 (3)。由 R236 定理 2，当原平台门 $P_2''=0$ 已付时，零通量方程

$$
(A_fu')'-V_fu=G_{H_{\mathrm E}}'',\qquad
A_f=6pp''-2(p')^2,\qquad V_f=6(p'p'')',
\tag{15}
$$

的全部零端通量分支

$$
u=p\left(C_0+
\int_{t_*}^{t}\frac{\int_0^s p(z)G_{H_{\mathrm E}}''(z)\,dz}
{A_f(s)p(s)^2}\,ds\right)
\tag{16}
$$

都可光滑延拓。不同 $C_0$ 只差全平项 $C_0p$。

该光滑结论没有把 $u(0)$ 强制为零，也没有授予非零通量支路光滑。若 $V=t^4B_{H_{\mathrm E}}$，R236 仍给

$$
u(0)=-\frac{V(0)}{3c^2}.
\tag{17}
$$

本次只求严格负幂，未求 $V(0)$，所以不报告未计算的端点数值。所有 $p^3\mathscr A$ 及更高局部次数的项已经由 R226 的精确端点积分定理自动处理；没有必要为了这个 germ 再开一个三次或四次层计算。

## 5. 七个必要原输入与继承关系

本次只恢复缺少 portable 原 DAG 的必要原根，逐一匹配原 SHA。没有重建完整权零空间或原评价矩阵。

| 原根 | 原标签 | 原项数 | 原 mixed $-2$ SHA256 |
|---|---|---:|---|
| $C_2$ | F0，state $(0,2,0,0)$，真权 0 | 1633 | b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f |
| $R_0$ | $p_0,W_7$ | 800 | b0bae8bad7bd7eaae8e0aad0eac1408b5aecd51f2bca5e12578395388e0af796 |
| $R_1$ | $p_0,W_{17}$ | 1060 | c9e2c99b259979e9a783c69622e929c7254eeb5bafb6631bf4d0f792b69ff81e |
| $R_2$ | $p_1,W_1$ | 1047 | d0fffba432e8a26a063f1d7d618f1b352a0d3c661af236e08c7b71323a057120 |
| $R_3$ | $p_1,W_{12}$ | 549 | 1cbdd945922696c4ce47c50e0c67894ef8ed673b8b195d7c1a08387b89207b4b |
| $R_4$ | $p_1,W_{16}$ | 1216 | f62bfd17fb145469826fb310b8c33ef8aceb9ff3e275d93e024c750f0b8b454c |
| $R_{10}$ | $p_2,W_{15}$ | 640 | 61cdde37cf3a136016cb71839e407becf18ece7fad68cf561401a6ba46569b34 |

$C_2$ 先按 R196 的同一 $\Gamma$ 组装，再取同一真权零原系数。其参考资料 SHA256 为
c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b。
完成式 (1) 后的完整 $H_{\mathrm E}$ 原 SHA256 为

**346ea2a14c74e4a6d831b05288533609b08bf7776782c0964dd66ece9eda96b6**，

与 R234 完全相同。输入来源分别为：

| 来源 | 原 run / source | 本次用途 |
|---|---|---|
| 完整静态原 export | 43645177423 / 2f1b809c0b0abb7a26303d36940edc203815f872 | 只取必要 W 与同 $\Gamma$ 的 $C_2$ |
| R126 旧响应定义 | 43649525432 / 5852d7d4400859e53dde789b4d63f200d0e0acce | 六条旧响应的标签、原 SHA 和来源 |
| R196 完整权零结论 | 43681388902 / 7872857e7750e1b5091560b6362e52dd952bc6fa | 已证明的 $\lambda_+$ 与空间身份 |
| R234 完成回执 | 43699241372 / ee9e2098c62392ddb709e7db26467bc225642d54 | 固定式 (1)、whole pure 零和一次层零 |

实际记录为：新科学目标 1、新二次目标 1、新 $N$ 收缩 0、新 profile 评价 0、新响应比较 0；其余十条旧权零响应未恢复，旧十七个一次层未重算，旧 cubic/whole-quartic normalizations 和 pure 查询均未重做。

## 6. 新人工、执行成本与复现身份

### 6.1 本次公开开发检查

同一源码公开执行了 **12 项新的人工检查，全部通过**。它们只查新二次截断接口：$J=3$ 的精度界、$J=4$ 必须保留的 $b_5$、原积分正号、两层嵌套积分、外多项式 $x=a_*+t$、真实二次 derivative/shuffle、word 内部 jets、$J\le2$ 自动零边界、局部次数守恒以及不重旧目标。

人工阶段没有读取真实输入，也没有评价 $H_{\mathrm E}$。它耗时 0.012286358 秒，峰值 RSS 27.64453125 MiB。没有把此前其他源码版本的人工重复计成本次通过。

### 6.2 唯一研究目标的实际成本

完整研究阶段耗时 **5.266248177 秒**，峰值 RSS **111.9921875 MiB**。

literal.Budget 所监测的整数操作计数为 **33930**，其所监测操作的最大位数为 **3**。这两个字段不是七根恢复、原 DAG 构造及 Python 全部有理运算的总次数或全局最大位数；例如同 $\Gamma$ 的原组合已包含更大的整数，不能把该位数字段误读为整个计算只用三位整数。

raw mapper 另记录 **42908** 次内部操作/插入，1019 次正次数左增量积分和 44 次次数零左积分，最多同时 27 个 series keys。该计数也不冒充全部研究算术的总成本。

### 6.3 可复现运行

- run：43701766182，attempt 1。
- job：132774268375。
- lane：character_zero_quadratic_endpoint。
- source：623f1c00d5a3f879e574b0d666213e751805186c。
- [完整公开 job 日志](https://github.com/Rogerhu12/math-research-public/actions/runs/43701766182/job/132774268375)。
- [metadata-only receipt](../notes/actions-43701766182-1-character_zero_quadratic_endpoint/receipt.json)。

主脚本 [literature_character_zero_quadratic_endpoint.py](../scripts/literature_character_zero_quadratic_endpoint.py) 为 19104 字节，SHA256
98e8caae918822b95f8f298ed9397f498b97e0cd5aaa0d1ebcec76b137300f3e。

新 helper [literature_endpoint_quadratic_principal.py](../scripts/literature_endpoint_quadratic_principal.py) 为 21175 字节，SHA256
01efa75bbb691c802e211ddf08fc3804d657af73d53ce428f51ae8b1ef365215。

本文消费的主文、人工和内存证书身份为：

| 输出 | 字节数 | SHA256 |
|---|---:|---|
| 研究主文 | 21366 | 7018931065f0231cdbbce4ce0188291fc431a44ed6d42a3529b5cb734379a251 |
| 12 项人工主文 | 9078 | 0be7cb85ddc593af6a78d023ed106e425e6032e2dde28f734a3e3f55e09ecdb9 |
| 仅内存证书 | 13749 | 91eeb3134776360d4e3f5e56f77a0085e33a325bc0611f441e517856317f2594 |
| 已发表 receipt | 50775 | 37c4c8cbce0fe0410d4f3f823a1f784e39245a48dd02a46cb80f83bb54a61072 |

receipt 与主文内 28 个不同源码依赖的大小和 SHA 对齐；主文和人工的 run/source 也与 receipt 相同。根 README 第 15 条下，研究主文和证书没有保存为仓库数据、Release 或 artifact。真实结论由公开 stdout 和上述脚本参数复现，SHA 元数据本身不是数学验证。

研究参数为：

~~~text
--static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
--R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation
--head-directory topics/visible-flex-new-mechanism/notes/actions-43681388902-1-character_head_zero
--first-layer-directory topics/visible-flex-new-mechanism/notes/actions-43699241372-1-character_zero_endpoint_layer
--max-seconds 240 --memory-mib 1024 --integer-bits 8192
--max-profile-jet 8 --max-terms 100000 --max-IBP-calls 300000
--max-cache-entries 250000 --max-summary-bytes 95000
--max-certificate-bytes 8000000
--output @OUT@/character-zero-quadratic-endpoint.json
~~~

@OUT@ 是 runner 临时目录，不是要求保存重算数据。公开开发入口为 --toy-only --max-seconds 60 --memory-mib 512，输出同一临时目录下的 development 主文。

## 7. 现在准确付清与尚未付清的门

同一个非零 $H_{\mathrm E}$ 同时满足

$$
\boxed{
\pi H_{\mathrm E}=0,\quad
\lambda_+(H_{\mathrm E})=1,\quad
\mathfrak T^\uparrow_{0,-2}(H_{\mathrm E})=0,\quad
\mathfrak B^\uparrow_{0,-2}(H_{\mathrm E})=0.
}
\tag{18}
$$

因此把这一特定一次层和二次主部联合使用，仍不能在相应权零 pure 零子空间上读出 $\lambda_+$。这个结论不撤销 R196 的完整正字符，也不把它延伸成所有端点、全部权或固定圆上的因子化结论。

还必须单独判断同一原代表的真实 $P_2''$。该平台门没有被本次 degree-two 主部处理，也不能因式 (18) 而默认通过。即使它通过，R225 的其他端点、每包总通量、内部 $p/A_f$ 退化、右锚匹配和同一个合法 $w$ 的全部矩条件仍是独立义务；完整 period 与 ruling 的联立也仍未完成。

下一必要工作据此收缩到真实平台与完整 range，不再为此 germ 重做已自动光滑的 $p^3\mathscr A$ 以上层。
