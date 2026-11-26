# R1057：原 p47 指定最低 CM 读数的三路完整认证

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**公开执行已证明：在原 $p=47$ 输入上，保留完整 $Q^2$ 的指定向量 $c=DQ(1-Q)\lambda$ 非零，且 $C_{\rm CM}(T_c)=15\in\mathbf F_{47}^{\times}$。** R1052 的整个原 CM 轮廓在此输入的首个非零 $w$ 次数为一。本篇只是一条固定输入结论，不推出全 $p$ 单位，不声称 $47$ 已满足 R1037 的未显式常数 $C_*$，也不据此关闭该层全部有理点或 Serre 主目标。

## 1. 固定原输入与结果

同 R1037、R1045、R1052，取
$$
p=47,\quad N=7,\quad \ell=16,\quad \deg A=22,\quad r=1-b^3,
\qquad \lambda=-6(b+1)/r.
$$
$A=bQ(b^3)$ 取原单首 Hasse 多项式，$\lambda$ 在 $A$ 根集上的类使用唯一次数小于 $22$ 的代表。原系数固定算子是
$$
Q(a)=\operatorname{quo}\bigl(r^{4N+2}a(b^p),A^2\bigr)\bmod A,
\qquad c=DQ(1-Q)\lambda.
\tag{1057.1}
$$
先作完整多项式除法，再模 $A$；没有先把分子模 $A^2$。外部系数保持不变。实际计算经过的最高完整多项式次数为 $1077$。

公开 stdout 的紧凑结果为：

| 原读数或检查 | 认证值 |
|---|---:|
| $c$ 是否零 | 否 |
| 留数公式 $C_{\rm CM}(T_c)$ | $15$ |
| 实际参数反演 $[Z^{15}](T_c/A)(B_{\rm CM}(Z))$ | $15$ |
| 全部超奇异点的 $2B(c,L_{\rm CM})$ | $15$ |
| 原配对 $B(c,(1-Q)\lambda)$ | $0$ |
| 完整轮廓的非零系数数目 | $14$ |
| 完整轮廓的首个非零 $w$ 次数 | $1$ |
| 完整 quotient 与微分表达交叉核次数 | $4$ |

所有完整数组只存在于 runner 内存，不入库，不上传 artifact 或 Release。结果保存必要标量与可复查的 source、request、summary hashes。

## 2. 三路为何读同一个实际对象

第一路直接用 R1052 的真实最低泛函：
$$
C_1=-\frac{3^{15}}{A(1)}
[r^{15}]
\frac{T_c((1-r)^{1/3})}{(1-r)^{5/3}j(r)^3}.
\tag{1057.2}
$$
这里只需 $j$ 的 $0,\ldots,15$ 次安全系数，未跨其首次坏分母。

第二路先形成同一实际 period 参数
$$
Z=-\frac r3\left(\frac{q(r)}{j(r)}\right)^3,
$$
逐项反演求 $r=r(Z)$，再代入 $b=(1-r)^{1/3}$ 和完整 $T_c/A$。所得
$$
C_2=[Z^{15}](T_c/A)(B_{\rm CM}(Z))
\tag{1057.3}
$$
来自复合反演，独立于第一路的 Lagrange 留数提取。

第三路独立形成
$$
L_{\rm CM}=\operatorname{PP}_{b=1}
 \frac{Z_b'}{Z^{16}}.
$$
程序保留其全部 $2,\ldots,16$ 阶极部，并检查简单极部为零。因 $A$ 单首且根简单，全根 trace 用精确插值恒等式计算：
$$
C_3=-\sum_{A(s)=0}\frac{T_c(s)L_{\rm CM}(s)}{A'(s)}
=-[b^{21}](T_cL_{\rm CM}\bmod A).
\tag{1057.4}
$$
这完全包括所有超奇异点，不取部分根、不以一个单独测试行代替 $c$。R1052 已证明 (1057.2)–(1057.4) 的原几何尺度及完整 self-return 来源。

每次 $Q$ 的完整除法还与 R1037 的 $LT/(2rA')$ 表达交叉比较，并核对完整余式 $TA'-T'A$。程序分别构造 $Q\lambda$、$Q^2\lambda$ 与 $Q((1-Q)\lambda)$，核线性一致性，保留原 $D$。因此本结果不是 R1054 中测试行 $T=b^2$ 的重算，也不是裸 $f_N$、核范数或任意最低列的值。

R1052 的轮廓系数除这些 Taylor 读数外只乘已保留的非零单位 $\kappa_1^k c_k\lambda_0^{-(\ell-k)}/(2m)$。故此处 $C_1=15\ne0$ 严格给首个非零 $w$ 次数一；未将这些几何单位设成一。

## 3. 原来源、公开执行和完整性

- 源提交：[9543f2ef1988a3fad40cf7d3f83102391dcb0de1](https://github.com/Rogerhu12/math-research-public/commit/9543f2ef1988a3fad40cf7d3f83102391dcb0de1)。
- [公开 run 45880257064](https://github.com/Rogerhu12/math-research-public/actions/runs/45880257064)，job **140117536918**，attempt 1，全部步骤 success。
- execution id：original-actual-p47-lowest-20261127-v1。
- [方法及预算](../notes/2026-11-27-original-p47-lowest-functional-method.md)、[实际 consumer](../scripts/original_p47_actual_lowest_functional.py)、[固定请求](../notes/original-p47-lowest-functional-request.json)。
- 数学总预算 $120$ 秒，实际 final receipt **0.06698969999999349 秒**，status complete、within_budget true；outer job 五分钟。
- 本地没有执行数学。root 与 o2_high_coefficient 已对精确源提交的全部代码作独立纸核，确认截断、全 quotient、$Q^2$、$D$、全余式及三读精度；root 实际读取 CONTRACT、SUMMARY、OUTPUT_RECEIPT、BUDGET_RECEIPT 和 job success，另以纯文本 SHA-256 核对整个 canonical SUMMARY 与公开 receipt 相等。
- 新请求仅触发一个独立工作流；已完成的 scalar 窗口未重触发。

| 固定项 | SHA-256 |
|---|---|
| consumer | f4ca20109a960de0b0f31e1bb0aa622feaadc0400125b69c4493304026d0ea59 |
| request | 02a71c8d435bfadffe74f8ea511bc668a530c6cb572d90b8e1922d928b4427b4 |
| method | 7982937f6583c9e23d28bfd6fbb1b4e243b4146b4f73e052d1f0b73fa1970a4c |
| root README | 581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 |
| topic README | 6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5 |
| R1037 | 6a8cb48d20f99b41fab4241f5a213d1506d603df10011ce16d8cb901bbd00b26 |
| R1045 | 3d6a0d7be3a2148f9447776c3947dafaad51f95ba6b7739a4016b844a3f72cdd |
| R1052 | 3b102a00f8914ae4aa6ec8cb87b2ff837032bebba5f4178f0a5ce4636b133aa5 |
| 原输入内存数组 | 828a153ebb23bcf687d1d55d42edbbc6613383617572ff729a5a24f9aeac5c59 |
| 完整指定 $Q\lambda,Q^2\lambda,v,c,T_c$ | 9974f006863557d881b427f7c910a0570f4f30f2dd5fb363599e124815b5d9b4 |
| 实际参数与全部最低极部 | bd09c406badda66797effe881aa10c17430b4527ea61ee8fe421d221001c1297 |
| canonical SUMMARY | 4c2bbe097e1b450bc4326b839e9d62adc866315ed7ab938a6c10db252c6c15cf |

SUMMARY 的 elapsed_seconds 为 0.06693752299997868；final receipt 包括随后序列化、输出及末次预算检查，所以两时长不同且均真实。程序是固定有限域精确算术，不含浮点数学；时钟小数只用于预算。

## 4. 消费边界

本篇支付了此前没有计算的**原指定行**在一个素数的最低读数。R1054 仅否定最低列恒在 $Q$ 核的候选；两篇读数和用途不同。此请求已经完成，不重开，不扩成重复旧窗口。继续任务是证明全范围的实际 $2B(v,QD L_{\rm CM})$ 或换用足以排深盘有理点的完整输入，以及 open.md 的其余全局分支；主目标仍 OPEN。
