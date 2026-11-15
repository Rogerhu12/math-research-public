# R196：完整权零字符头部、唯一正射线与 canonical 零矩成本的严格长度障碍

日期：2026-11-15。**完整原式计算已在本公开仓库 GitHub Actions 完成；正性分类及长度恒等为本文纸面推论。** 推导、消费器与整理：tail_cost；root 独立读取完整实际摘要并核对参数 action 与长度恒等。本文对所述结论负责，不把正字符在 universal canonical 空间上的存在扩大为任意固定第一圆或任意新增二阶自由函数的障碍。

## 1. 结论及适用范围

记 $U=\mathcal U_4$、$R=\mathcal R_8$，使用既有完整 canonical 两相位、共同右锚和全部实际历史。$U_\sigma,R_\sigma$ 表示 profile 真缩放权子空间；$N$ 是既有输入平移的无穷小生成元。本次完整计算得到

$$
\boxed{
\dim U_0=19,\qquad
\dim R_0=16,\qquad
\dim(U_0/R_0)=3,
}
\tag{1}
$$

$$
\boxed{
\dim (R_0+NU_1)/R_0=1,\qquad
\dim H_0=2,\qquad
H_0=U_0/(R_0+NU_1).
}
\tag{2}
$$

这些是真实函数空间及其商的维数，既不是字面 DAG 秩，也不是只保留若干必要等式的外空间维数。两维头部在计算中没有预先施加正性或正字符乘子条件。

令 $\lambda_{x,y}$ 是后文明确给出的全部真实权零仿射字符。其在真实闭成本锥上的非负条件恰为

$$
\boxed{y=0,\qquad x\leq0.}
\tag{3}
$$

因此权零非负字符构成唯一射线

$$
\mathbb R_{\geq0}\lambda_+,\qquad
\lambda_+=\lambda_{-1,0}.
\tag{4}
$$

该泛函在任意正时长、相同常数 germ、闭 frame、零八矩的完整 canonical 成本上满足

$$
\boxed{
\lambda_+(V_B)
=\int_B k(s)^2\,ds
=L_B+\int_B\left(\frac{h_s}{h}\right)^2ds
>0.
}
\tag{5}
$$

特别地，非空实际 $M=T=0$ 字的 universal canonical 第四成本不能等于零。式 (5) 的严格性来自真实零矩条件，不需要假设 $k$ 逐点非零。

这已经给出一个真实正字符，故不能继续以“所有权的正字符都会消失”为前提寻求 universal 成本锥等于整个 $U$。另一方面，固定 profile 的代入可能有核，新增独立二阶自由函数也可能改变允许的成本空间；本文没有支付这两个扩展问题。第 8 节准确说明这些边界。

## 2. 唯一实际运行、来源与复现约定

实际运行：

- run：43681388902；
- source：7872857e7750e1b5091560b6362e52dd952bc6fa；
- job：132712596579，character_head_zero；
- [公开 Actions job](https://github.com/Rogerhu12/math-research-public/actions/runs/43681388902/job/132712596579)；
- [公开 metadata-only 回执](../notes/actions-43681388902-1-character_head_zero/receipt.json)；
- [唯一新消费器](../scripts/literature_character_head_zero.py)；
- [完整输入与设计说明](../notes/character-head-zero-complete-consumer-design-20261115.md)。

消费器为 42361 字节，SHA256：

$$
\texttt{337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4}.
$$

该 source 先公开执行十项新人工开发检查，全部通过，再运行实际研究目标。旧人工套件、旧原 profile 评价、旧 forcing 和旧同权目标均未重复。

| 项目 | 字节 | SHA256 |
|---|---:|---|
| 公开 metadata-only receipt | 45501 | 7919e2406650d394b1128d7014585dbdb830a87adb7979e74f6b2e752e484abf |
| 实际 stdout/runner 临时完整摘要 | 25121 | 838266c7b4b86b137482127e7e874d8d3eb014aa5745b9be6fceb2d9d3dc7fa4 |
| 新十项人工的 stdout/runner 临时摘要 | 7874 | 91ed8ad536fcf1e63879e5f2d3386846f2ca4bcfb1dc3c680d979be094a3c1c3 |
| 实际内存完整证书 | 63029 | aeb58ea3da3945bd6dc72c13d64d85e88a0cf2238d4ba705bf3989678831909f |

实际完整摘要已从公开 stdout 提取，并逐字节核对回执所记尺寸和 SHA。实际 elapsed 为 10.240285569 秒，峰值 RSS 为 316.71484375 MiB；完成 8460 次精确整数操作，最大整数位数 33。新人工 elapsed 为 0.002540967 秒。

遵守当时根 README 第 15 条，新可重算证书、数据与 Actions payload 不在仓库、Release 或 artifact 中保存。上表后面三个对象是 stdout、runner 临时对象或内存对象的身份，不声称存在同名仓库文件。完整复现依据上述冻结脚本、source、run、参数和 SHA；公开仓库只保存允许的 metadata 回执。

实际参数为：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_character_head_zero.py \
  --static-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient \
  --factors-directory topics/visible-flex-new-mechanism/notes/actions-43651096112-1-local_fourth_derivative_factors \
  --acceleration-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
  --cache-directory topics/visible-flex-new-mechanism/notes/actions-43665345551-1-character_head_minus2 \
  --R0-directory topics/visible-flex-new-mechanism/notes/actions-43649525432-1-g_first_translation \
  --max-seconds 240 \
  --memory-mib 1024 \
  --integer-bits 8192 \
  --max-terms 150000 \
  --max-IBP-calls 500000 \
  --max-cache-entries 500000 \
  --max-summary-bytes 95000 \
  --max-certificate-bytes 16000000 \
  --output @OUT@/character-head-zero-result.json
```

其中 @OUT@ 是 runner 临时目录；它不改变数学输入。

### 2.1 新运算的准确范围

五个既有输入的来源、原 SHA 和发布回执均由冻结消费器绑定。新增范围如下。

1. R126 的 16 个真实独立 $R_0$ 响应原 DAG 当时没有 portable 导出。本次只恢复这 16 个缺失原根，完整两模式共 32 个原 hash 全与旧记录匹配。旧原下标为
   $0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19$。
   不重算旧四条依赖、旧 NF 或旧 16 阶原评价。
2. 读取已发布因子和既有投影缓存：选中 15 个原 N 记录，其中 10 个非零已存投影、5 个已证明为空的 N0 真权零投影。新 N 投影次数为零。N0 的参考态常数扣除完整保留。
3. 只对本权所需的 v2/v4 原根作新投影，并复用已发布加速度层原根。没有重编 3974 因子、几何微分或旧 forcing。
4. 实际只新增 11 个完整 $E\times N$ 收缩；完整去重计划 SHA 为
   fa961aaf6cb4872f0be89300029732155808508cb09adadfd3e30b4cd0939156。
5. 从这些原项装配全部十四个正规函数族、同一个 $\Gamma m_0/\Gamma m_2$ 修正和完整八个 D 记录。八个参考态的静态值全部准确为零；D 使用 $\partial_\omega$ 减同一个低层 cocycle，不能用单独 $\partial_\omega$ 替代。

该范围使用 [R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md) 和 [R192](R192-weight-zero-character-multiplier-and-first-order-action.md) 已证明的模 $R$ / 模 $W$ 谱缩减。它不把这些商关系改写为未证明的原 DAG 点态相等。

## 3. 完整函数核及真实头部

十四族在本权留下 22 个状态系数记录：

| 族 | 记录数 |
|---|---:|
| F0 | 10 |
| Q2_0 | 1 |
| Q2_1 | 3 |
| Q2_2 | 6 |
| A_hh | 1 |
| Q4_4 | 1 |

其余八族在本次完整同权呈示中为零；不是尚未计算的缺项。保留 Q4_4 的原记录，即使它最终在字符商中取值为零，也没有在函数核计算前删掉它。

将 16 个真实 $R_0$ 原根排在前面，再接 22 个 normal 原根，得到 38 列。对每列同时保留 pure 根和 balanced 根；使用 R159 的两根共同忠实性，不假设 pure 单独忠实。

新共同固定颜色表示有 318 行，精确矩阵秩 19，完整核有 19 条关系。列序从零开始，保留基为

$$
0,1,\ldots,15,\ 18,\ 20,\ 22.
\tag{6}
$$

即 16 个真实响应与 normal 记录 $C_2,C_4,C_6$。R126 已证明前 16 个响应真实独立，本次原根 hash 恢复与完整共同表示一致；不能从字面 DAG 独立代替这项来源。

所有新列的原式到共同表示转换均完成，转换 SHA 为

$$
\texttt{4f135aab9b9a384ee8a433ddad0993db9c8dd1b7d7e4077acafdb81d54b44daf}.
$$

完整 19 条原函数关系 SHA 为

$$
\texttt{da553ab6b7bc71903928f86b8b28bd26443ef72c1aef90414b949bf62d512c79}.
$$

R178 给出固定颜色转换的 sound 恒等及终止，R179 给出规范余 letter 的完整 word 表示真实单射；实际所有列满足所需语法。结合 R159 的 pure/balanced 忠实性，矩阵核恰是本次完整呈示的真实函数核，而非仅一个可证关系子集。实际记录 1405 次 primitive 调用、892 次固定颜色 IBP、2161 次严格下降检查、96 次带非空余 word 的多项式 IBP，cycle fallback 为零。

R130 的完整正规系数 span、R163 的同一 cocycle 和全部八个 D 记录随后给出 (1)–(2)。这里只用了完整函数关系和平移分母，没有先加入 positive 必要条件。

也可从结果准确描述这一步商：$U_0/R_0$ 的基可取 $[C_2],[C_4],[C_6]$，而一维平移像正是 $[C_6]$ 所张成的线。这个说法由完整基 (6)、后文全部头部赋值及商维数共同推出，不需要新增消元。

## 4. 全部两参数字符及二十二个准确赋值

状态键采用

$$
(h\text{ 的幂},\ k\text{ 的幂},\ \omega\text{ 的幂},\ \log h\text{ 的幂}).
$$

令 $\nu_j=\lambda(C_j)$。自由 normal 下标为 5 和 20，记

$$
x=\nu_5,\qquad y=\nu_{20}.
\tag{7}
$$

全部赋值如下；零值是完整原函数核与 D 后的准确结果。

| j | 族 | 状态键 | $\nu_j$ |
|---:|---|---|---|
| 0 | F0 | $(-1,1,0,0)$ | $0$ |
| 1 | F0 | $(-1,3,0,0)$ | $0$ |
| 2 | F0 | $(0,2,0,0)$ | $-x-y$ |
| 3 | F0 | $(0,2,1,0)$ | $0$ |
| 4 | F0 | $(0,4,0,0)$ | $y$ |
| 5 | F0 | $(1,1,0,0)$ | $x$ |
| 6 | F0 | $(1,1,1,0)$ | $0$ |
| 7 | F0 | $(1,1,2,0)$ | $0$ |
| 8 | F0 | $(1,3,1,0)$ | $0$ |
| 9 | F0 | $(2,2,2,0)$ | $0$ |
| 10 | Q2_0 | $(0,0,0,0)$ | $-y/3$ |
| 11 | Q2_1 | $(-2,0,0,0)$ | $0$ |
| 12 | Q2_1 | $(-1,1,0,0)$ | $-11y/3$ |
| 13 | Q2_1 | $(0,0,1,0)$ | $0$ |
| 14 | Q2_2 | $(-2,0,0,0)$ | $y$ |
| 15 | Q2_2 | $(-2,0,1,0)$ | $0$ |
| 16 | Q2_2 | $(-2,1,0,0)$ | $0$ |
| 17 | Q2_2 | $(-2,2,0,0)$ | $-4y/3$ |
| 18 | Q2_2 | $(-2,2,0,1)$ | $0$ |
| 19 | Q2_2 | $(-1,1,1,0)$ | $0$ |
| 20 | A_hh | $(-2,0,0,0)$ | $y$ |
| 21 | Q4_4 | $(-4,0,0,0)$ | $0$ |

这张表与杀掉全部 $R_0$ 一起，定义每个 $(x,y)\in\mathbb R^2$ 对完整 $U_0$ 的良定义线性泛函。加入完整 D 后它杀掉 $NU_1$。再令

$$
\lambda_{x,y}(V)=\lambda_{x,y}(\Pi_0V)
\tag{8}
$$

即得到完整 U 上杀 R、输入平移不变、真缩放权零的仿射字符。这里只用完整有限权分解；不是把一个系数赋值不经函数关系检查就扩张到 U。

本权同一静态 cocycle 的向量按
$(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$ 排列为

$$
c=(0,0,0,0,0,0,0,0),\qquad
d=(0,0,-2x,0,0,0,0,0).
\tag{9}
$$

尤其 R192 的协变乘子存在条件 $d_{p_1}=0$ 对**整个真实两维头部**自动成立，而非只对正锥成立。

## 5. 同一个八矩乘子及完整 action

采用 [R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md) 与 R192 的坐标。这里 R192 的 $\beta=d_{p_2}/2=-x$。所有相容的协变乘子可写为

$$
\mu_\alpha=(0,2\alpha,-2x,0,0,0,0,8\alpha),
\qquad \alpha\in\mathbb R.
\tag{10}
$$

$\alpha$ 是选择同一乘子的自由度，不是新增的第三个头部坐标。

其矩阵作用为

$$
\mu_\alpha m_0=\alpha(k^2-1)+xkh,\qquad
\mu_\alpha m_2=-\alpha\left(\frac{h_s}{h}\right)^2.
\tag{11}
$$

令

$$
r=\log h,\qquad p=r'.
$$

路径两端为常数 germ，所以 p 及需要的高阶导数在两端为零。表中静态项为

$$
\lambda F_0=-(x+y)k^2+yk^4+xhk.
$$

扣掉 (11)，并使用准确正规式，完整 action 成为

$$
\boxed{
\begin{aligned}
I_{\lambda_{x,y},\alpha}[p,k]
=\int\bigg[
&y(p')^2+yp^4-\frac y3(k')^2
-\frac{11y}{3}kp\,k'\\
&+\left(\alpha+y-\frac{4y}{3}k^2\right)p^2\\
&+\alpha-(\alpha+x+y)k^2+yk^4
\bigg]\,ds .
\end{aligned}
}
\tag{12}
$$

其中 $h>0$ 由 $r'=p$ 恢复，真实约束始终为

$$
\omega'=\frac{k'}{2h}.
\tag{13}
$$

没有把 $\omega$ 当作独立的常值控制。式 (12) 已消掉它的显式出现，是完整函数关系及同一 cocycle 后的结果。

最高项的处理也保留了边界：A_hh 贡献

$$
y\,h^{-2}(h_{ss})^2=y(p'+p^2)^2.
$$

其交叉项积分为

$$
2y\int p'p^2\,ds=\frac{2y}{3}[p^3]_{\mathrm{两端}}=0,
$$

从而得到 (12) 中的 $y(p')^2+yp^4$。Q4_4 的字符值为零，这里没有遗漏一个仍待支付的 quartic 项。

按 [R194](R194-weight-zero-free-time-criterion-and-zero-acceleration-boundary.md) 的一阶 action 记号，完整系数是

$$
\begin{aligned}
a=c&=y,\\
b_0(k)&=-y/3,\\
b_1(k)&=-11yk/3,\\
b_2(k)&=\alpha+y-\frac{4y}{3}k^2,\\
A_0(k)&=\alpha-(\alpha+x+y)k^2+yk^4.
\end{aligned}
\tag{14}
$$

特别地，磁项 $b_1p\,dk$ 没有被省略。

## 6. 全部真实非负字符恰为一条射线

[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md) 给出完整实际成本非负与某个**固定同一乘子**下全部允许有限平端开路径 action 非负之间的等价。R192 支付了本权乘子的形式。因此可以在 (12) 中使用真实开路径作必要性检验，也可以用逐点非负证明充分性。

### 6.1 必有 $y=0$

首先 $y\geq0$。若 $y<0$，固定 $k=0$，取一个非平凡紧支撑平滑 r-bump 并压缩时长 $\varepsilon$。$h=e^r>0$，所有端点保持平坦；(13) 允许取常 $\omega$。式 (12) 的最高部分为

$$
y\int\bigl((r'')^2+(r')^4\bigr)\,ds,
$$

按 $\varepsilon^{-3}$ 缩放且严格为负，其余二阶和零阶分别至多按 $\varepsilon^{-1}$ 与 $\varepsilon$ 缩放。充分小的有限 $\varepsilon$ 给真实负 action，矛盾。

其次 $y\leq0$。令 h 为常数，即 $p=0$，取一个非平凡紧支撑 k-bump 并压缩时长 $\varepsilon$。其 action 是

$$
-\frac y3\int(k')^2ds+\int A_0(k)\,ds.
$$

若 $y>0$，第一项按 $-\varepsilon^{-1}$ 缩放，第二项按 $\varepsilon$ 缩放，故有限小 $\varepsilon$ 给负值。(13) 此时积分为 $\omega=k/(2h)+\text{常数}$，k 的平端与返回保证真实 $\omega$ 端口正确。

两者合并得 $y=0$。这一步不使用假的“磁项二次矩阵半正定必要条件”，也不需要任何新路径数值评价。

### 6.2 剩余一参数的充要条件

$y=0$ 时 (12) 化为

$$
I_{\lambda_{x,0},\alpha}
=\int\left\{\alpha p^2+\alpha-(\alpha+x)k^2\right\}\,ds.
\tag{15}
$$

对于同一固定 $\alpha$，全部有限平端开路径非负当且仅当

$$
\alpha\geq0,\qquad \alpha+x\leq0.
\tag{16}
$$

必要性：$p=k=0$ 的长常段迫 $\alpha\geq0$；$p=0$ 的任意大常值 k 段迫 $\alpha+x\leq0$。如需把这些段接到统一固定外端口，只需先固定该常值和有限平坦连接，再延长常段；有限连接成本不改变结论。

充分性：在 (16) 下 (15) 的三个系数逐点非负，故其积分对每条真实允许路径非负。

存在满足 (16) 的 $\alpha$ 当且仅当 $x\leq0$。当 $x\leq0$ 时直接取 $\alpha=0$ 即可。由 R140 的充分性，这不是有限测试的可行外点，而是整个真实成本锥上的非负泛函。非零头部对应 $x<0$，从而得到 (3)–(4)。

## 7. 规范化正字符的实际零矩成本

取

$$
\lambda_+=\lambda_{-1,0},\qquad \alpha=0.
$$

在完整 normal 表中它只在两处非零：

$$
\lambda_+(C_2)=1,\qquad
\lambda_+(C_5)=-1.
\tag{17}
$$

其余二十个 normal 值与全部 16 个响应值为零。为便于后续准确识别，其两个 F0 原根的双模式 SHA 为：

| 根 | 模式 −4 | 模式 −2 |
|---|---|---|
| $C_2$ | ad4cd7fcdcbac89c55309c6906b6cb3a6d869ad37834e4a32fe8cad1b6e33393 | b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f |
| $C_5$ | 8994aa18cef35bc4af10eabca3f0ec87fc4034db93d16c9a5c5a3b76aff36868 | f758bb46f8d6c08c7b014696aac81f1ed62ed312366b0f94058445fd4fedb684 |

这张赋值表通过第 3 节真实函数核定义 $\lambda_+$，尚不等于一个已经找到的固定 profile 点值或分布公式。

此时同一乘子为

$$
\mu_+=(0,0,2,0,0,0,0,0),
$$

且

$$
\lambda_+F_0=k^2-hk,\qquad
\mu_+m_0=-hk,\qquad
\mu_+m_2=0.
\tag{18}
$$

故完整修正 action 准确等于

$$
I_{\lambda_+,0}=\int k^2ds.
\tag{19}
$$

R109 的局部化恒等、R130 的真实 span 和完整平端边界给出：在实际闭 frame、$M=0$ 成本上，$\lambda_+$ 杀掉所有 R 历史差，$\Gamma M$ 和 $\mu_+M$ 均为零，所以 (19) 就是 $\lambda_+(V_B)$。这一步不是仅把形式密度积分当作实际成本。

最后使用 R164 已支付的完整八矩原恒等

$$
p_1+4t_1
=\frac12\left\{k^2-1-\left(\frac{h_s}{h}\right)^2\right\}.
\tag{20}
$$

这里 $p_1,t_1$ 是矩阵坐标密度，与第 5 节的路径变量 $p=r'$ 不同。实际 $M_B=0$ 使 (20) 的积分为零，因此

$$
\int_B k^2ds=L_B+\int_B\left(\frac{h_s}{h}\right)^2ds.
$$

这证明 (5)，并说明对正时长零矩路径 $\int k^2$ 必严格为正。特别地，它不能因选择 $k=0$ 而消去：这样的正时长路径本身不满足零矩条件 (20)。

## 8. 对主线真正支付的结论与未支付范围

### 8.1 已支付的 universal canonical 障碍

完整真实正字符 $\lambda_+$ 杀 R、杀平移像，且在真实 canonical 闭成本上非负。它使完整成本闭锥位于一个真闭半空间，因此该锥不是整个 U。式 (5) 还说明每一个正时长有限 $M=T=0$ 字的 universal canonical 成本都非零。

这里不需要继续分类 −4、−6、−8 才能得出“存在非零正字符”。本文也不宣称取得统一的正距离下界：总时长趋零的极限问题与每个正时长有限字的严格性是不同命题。

### 8.2 固定第一圆必须另付因子化

对一个具体允许的 profile $(f,g)$，写实际代入映射

$$
\operatorname{ev}_{f,g}:U\longrightarrow \mathcal F_{f,g}.
$$

本泛函能下降为该固定 profile 输出上的良定义泛函，当且仅当

$$
\ker(\operatorname{ev}_{f,g}|_U)\subseteq\ker\lambda_+.
\tag{21}
$$

若 (21) 成立，则固定 profile 的 canonical 成本为零会由 (5) 导致矛盾。忠实 profile 自动满足 (21)；既有有限空间忠实实现定理可以用于适当选择的合法第一圆。但本文没有把“存在忠实第一圆”替换为“每个特殊第一圆都忠实”。

尤其某个 $V_B\ne0$ 作为 universal 算子仍可能在特殊 profile 上代入为零。要将 (5) 用于 R183 类型的特殊第一圆，须给出明确的输出读出或直接证明 (21)，不能凭原矩阵秩 19 推断。

### 8.3 独立二阶 gauge 的定义域

若进一步允许新增独立二阶自由函数 w，使第四成本改变为 $V_B+\Delta_w$，本文只已定义 $\lambda_+$ 在 canonical U 上的作用。必须先说明 $\Delta_w$ 是否属于同一空间、泛函是否延拓，以及它是否杀掉实际允许的 $\Delta_w$，才可把本障碍用于该扩大问题。

因此本文既没有禁止任意 w，也没有把 canonical 原势的固定选择误作题目允许的全部二阶修正。下一决定性的工作是固定 profile / 新 gauge 的因子化与局部输出读出；不是为了权重表完整而继续重复已经无助于此障碍存在性的计算。

## 9. 本文状态

完整 38 列原函数关系、全部十四族、同一低层 cocycle 和真 $H_0$ 均已完成。正射线分类及严格零矩长度恒等已由上述完整 action 逐步证明。本文没有宣称题目完成标准已经达到，也没有把 universal canonical 不可能性扩大为所有特殊 profile 或全部非 canonical 修正的不可能性。
