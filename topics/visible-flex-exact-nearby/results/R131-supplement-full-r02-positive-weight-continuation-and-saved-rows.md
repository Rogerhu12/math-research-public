# R131 补篇：原目标到五分之一的完整正权延拓

2026-11-13，visible-exact-astra-ac0d。

**状态：已证明并实际执行全部 579 个闭盒。** 同一原腰初值的真实
Codazzi 解在 $0\le r\le1/5$ 上存在，覆盖整个原参数盒和实角圆周。
它使用原完整径向度量；本条不更换目标、有限候选、权函数或初值。
本条结论是精确 Cauchy 延拓；几何嵌入、外帽匹配和最终闭面族另证。

## 1. 对象与已证明的比较定理

准确中心参数为
$$
\delta_*=-\frac{7789843107295549}{4611686018427387904},
\qquad |\eta|\le10^{-9}.
$$
度量仍为 $E(r)dr^2+a(r)^2d\theta^2$，其中 $E$ 是原完整
$|F_r|^2$ 的角平均，$a$ 不变。目标对象的 SHA256 为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
完整 BC 候选原字节 SHA256 为
`da1dcc9e5dbeff97998023db376c9e0c3fcfae48639cc1639dba57c7494c91a3`，
完整 s10 正权原字节 SHA256 为
`5f07d115179af334425e2585e60bbbd4c5acec7c5228c1c495cb21b71ea36ffe`。

采用[准确正权比较及清分母闭盒定理](R131-supplement-positive-comparison-weights-and-cleared-tube-rows.md)
的 (P.1)–(P.14)。特别，误差是两条真实 Riemann 场的误差：
$$
u=p-P,\quad v=q-Q,\qquad
P=(\widehat B+k)/\widehat C,\quad
Q=(\widehat B-k)/\widehat C,\quad k=\sqrt{-K},
$$
$$
z=\max\{\|u/W_p\|_\infty,\|v/W_q\|_\infty\}.
\tag{F.1}
$$
这里 $k$ 是真实目标量，候选和权函数的全部有限频率与 mean 均保留。
此前前193盒补篇中将 $z$ 写为 BC 误差是记号笔误；原程序一直消费
(F.1)，本次同时修正文稿中的记号，不改此前数据。

原283盒完整 cubic 残差提供每盒真实 $\rho_i$；同一有限候选与
同一完整正权的全部端点和 scalar germ 合并为579个准确闭盒。
每盒的4096个闭角区间覆盖完整实角圆周。全部有限乘积先在不混叠的
4096点代数内形成，再以有向 Taylor 余项覆盖整个角盒和径向盒。
真实参数、scalar 模型余项、完整分母以及管内所有一次和二次误差项
均按原定理支付，没有把有限 Fourier 计算当成未知解的截断。

## 2. 中断报告中已经保存的完整闭盒仍是有效证书

原 producer `fourfold_codazzi_positive_weight_cubic_native.py` 的一行
计算，先调用 `row_budget` 完成两个方程的全部正负号、五个原管、
完整标量余项和严格分母检查；只有函数正常返回后，才把完整行加入
`rows`，更新准确 `covered_interval` 并保存。行的有效性不依赖后面
尚未执行的行。最后的 `complete=true` 只确认计划终点已经到达，
其后没有新的数学条件用于补足此前各行。

因此，有效闭盒可以从明确保留的中断报告中逐行消费；全报告继续
保持 `complete=false`，不声称它完成了原计划。未保存的半行不能
使用。证明很直接：每个已保存行都是原完整闭盒算法正常返回的结果，
具有原定理的全部局部假设；证明完整区间只需要这些有效闭盒的并
准确覆盖区间，不依赖它们由几个进程产生。

本次实际记录如下。表内编号均为从0开始的原 partition 编号。

| 保存记录 | 已保存并消费的完整行 | 原进程状态 |
|---|---:|---|
| `batched-s10-r02-part-000a-native.json.gz` | 0–95，共96行 | 原计划完整，正常结束 |
| `batched-s10-r02-part-000b-native.json.gz` | 96–192，共97行 | 原计划完整，正常结束 |
| `cubic-s10-r02-part-001-native.json.gz` | 193–385，共193行 | 原计划完整，正常结束 |
| `cubic-s10-r02-part-002-native.json.gz` | 386–572，共187行 | 原计划193行，外部终止，exit137 |
| `batched-s10-r02-part-002-tail-native.json.gz` | 573–578，共6行 | 新请求完整，正常结束 |

这些文件的共同前缀是 `notes/2026-11-13-Codazzi-positive-weight-`。
第四份报告原 `complete=false,failure=null` 保持不变；进程观察及
完整已保存日志见
`notes/2026-11-13-Codazzi-positive-weight-cubic-part002-exit137.json`。
终端报告了 Killed 和 exit137，未由此断言数学失败或具体终止原因。
它保存的最后准确端点为
$3548836506367951/18014398509481984$，恰是新六行的左端。

## 3. 新消费者对完整并的准确检查

`fourfold_codazzi_positive_weight_saved_row_C0_v4.py` 使用新的输出
kind；旧 v3 和所有原生报告均不改写。它先核对原 producer、完整
目标/候选/权/初值身份、全部输入和依赖 SHA，以及原完整范围门。
任何中断报告还必须显式提供绑定其原字节、原请求、已存范围与
实际exit137记录的过程文件。

对每份输入，消费者从原283盒残差与完整权节点的准确有理数组重新
构造整个共同 partition，包含原进程尚未计算的行。原请求必须恰是
它声明的完整计划切片。逐已存行再核对准确 `native_row`、
`weight_piece`、两端点、scalar germ、原六项标量/残差界、五个管、
完整标量模型及正权条件。编号必须从0连续增加，不能重复或遗漏。
第四份输入的计划193行与已存187行分别保留；仅后者参与传播。
最终游标必须准确为 $1/5$，本次共消费579行。

这比旧“每份文件都必须完整”的合同更一般，但没有放宽每个实际
闭盒的数学有效性，也没有把中断记录伪装成完成记录。

## 4. 同一个真实误差与梯度连续传播

由原定理，每个闭盒上
$$
D^+z\le L_i z+\rho_i/w_i,\qquad L_i\ge0,
\tag{F.2}
$$
其中 $w_i$ 是同一个真实正权函数的闭盒下界。
长度为 $h_i$ 的闭盒采用严格仿射屏障，实际有向检查
$$
1-h_iL_i>0,\qquad
z_{i+1}-z_i>h_i(L_i z_{i+1}+\rho_i/w_i).
\tag{F.3}
$$
构造式为
$$
z_{i+1}=\operatorname{up}\!\left[
\frac{z_i+h_i\rho_i/w_i}{1-h_iL_i}(1+2^{-40})+2^{-180}
\right].
$$
全过程只有原腰的一次初始误差。共享端点使候选、正权和真实误差
连续，因此文件交界没有重置或重新归一化。闭盒末值直接作为下一
闭盒初值，并逐盒检查
$$
w_i^+z_{i+1}<T,\quad
d_i^{\rm cand}-2w_i^+z_{i+1}>0,\quad k_i^->0.
\tag{F.4}
$$
第一式是未加权真实误差门；小的 $z$ 不能替代它。

同时，从独立实际腰初值出发，只初始化一次
$\mathcal G=\max\{\|(p-q)p_\theta\|_\infty,
\|(p-q)q_\theta\|_\infty\}$。由
[R131真实线性退化输运](R131-linear-degenerate-weighted-gradient-and-C0-continuation.md)，
在 $|p|,|q|\le M_i$ 的闭盒中
$$
\mathcal G_{i+1}\le\mathcal G_i
\exp\{h_i[|\beta_i|(2+4M_i^2)+4|\kappa_i|]\}.
\tag{F.5}
$$
每盒真实角导数由 $\mathcal G/(q-p)$ 控制。严格正间隙、有限真梯度
与有界真系数给同一 Cauchy 分支的继续准则；第一退出论证与 (F.4)
闭合。这是完整未知解的比较，不需要候选 $C^1$ 误差屏障。

## 5. 实际执行的全区间结论

五个原管全部尝试，结果完整保存。

| 原管 $T$ | 全579盒结果 | 最大真实未加权误差上界 |
|---:|---|---:|
| $1/500$ | 原row537的真实管门不通过 | 不授完整区间 |
| $1/200$ | 全部通过 | $0.003887037041$ |
| $1/100$ | 全部通过 | $0.005361653333$ |
| $1/50$ | 全部通过 | $0.010495903451$ |
| $1/16$ | 原row528的真实管门不通过 | 不授完整区间 |

以最紧的通过管 $T=1/200$，整个 $[0,1/5]$ 上的向外取整界为
$$
\max(|p-P|,|q-Q|)<0.003887037041,\qquad
q-p>0.21117001608,
$$
$$
k>0.53198969829,\qquad
\max(|p_\theta|,|q_\theta|)<7561.596192.
$$
右端 $z<0.000036149818186$，真实加权梯度小于 $2352.448467$。
所有数值均来自完整有向包围，程序逐盒保留严格 margin 和各个真门。
原两份失败管的失败行及之前各行也保留，不将一次失败抹成成功。

完整输出为
`notes/2026-11-13-R131-positive-weight-complete-r02-C0-native.json.gz`，
SHA256 为
`0e04c11352951a00cd51c1af7e8b3c9014b9adfd6fb2432d181d7ac1ba2bb123`。
该记录直接绑定全部程序、五份原生记录、过程证据和原目标；重新
执行时必须使用新输出路径：

```bash
python scripts/fourfold_codazzi_positive_weight_saved_row_C0_v4.py \
  --native-parts \
    notes/2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000a-native.json.gz \
    notes/2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-000b-native.json.gz \
    notes/2026-11-13-Codazzi-positive-weight-cubic-s10-r02-part-001-native.json.gz \
    notes/2026-11-13-Codazzi-positive-weight-cubic-s10-r02-part-002-native.json.gz \
    notes/2026-11-13-Codazzi-positive-weight-batched-s10-r02-part-002-tail-native.json.gz \
  --interrupted-audits notes/2026-11-13-Codazzi-positive-weight-cubic-part002-exit137.json \
  --right 1/5 --out /tmp/complete-r02-positive-weight-new.json.gz
```

原始各行也可用两个原 producer 的相同4096网格和表列
`--first/--rows` 重做；第四份可一次完整重算193行，外部终止不是
该证明必须再现的数学事件。证明所需的是全579个有效闭盒。

R126 的同一周期框架和腰反射给真实等距浸入的重建。
本条尚未证明该更大环带的全局单射；帽/regular匹配、整闭面
可见位移、同度量非全等族和reach仍接着处理。
