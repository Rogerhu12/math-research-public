# R150：原九个 h0 目标的完整七维 socle 消费者

作者：ChatGPT（AI），literature_audit  
日期：2026-11-16

## 1. 已付前提与本次唯一问题

完整原 210 来源第四页已实际完成，剩余系数指数恰为 6。令 $p=31$、$D=\mathbb Z_{(31)}$、$C=N/\operatorname{im}A$。已付

$$
C\cong D^{298}\oplus(D/p)^2\oplus(D/p^2)^5
\oplus(D/p^3)^2\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6.
$$

原九个 $b_j=h_0t_j$ 已有精确 $p^2b_j\in\operatorname{im}A$，且完整任意次数的旧 $p^2$ 反证排除了 $b_j\in\operatorname{im}A$。本次只判定各 $pb_j$ 是否为零类，输出九个最小分母指数 1 或 2；不预设任何结果。

原目标始终为

$$
t_j=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,\quad 2\le j\le10,
$$

$$
h_0=s^3(s-2)F_+^2F_-^2E_8.
$$

不得把 $h_0$ 换为 $h_*=h_0/(s-2)$。

## 2. 完整七维判别

父计算已给 16 个原真除源 $g_i$，指数依次为

$$
(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6).
$$

其完整 315 类独立，实际阶数和为 50，因而与已付完整系数扭子模长度 50 夹等，给出完整系数直和分解。以下坐标使用这一原来源基，不能把规范化的另一 13 维基直接代入。

从旧已验证的全原多项式来源 $Z_j$ 开始：

$$
r_3=(pb_j-AZ_j)/p^3.
$$

用真实前 13 个来源解全 315 恒等式 $\bar r_3=\bar G_{13}a$。完整原正常形与单位解给

$$
r_3=G_{13}a+Aq_3+pr_4.
$$

再用真实前 15 个来源解 $\bar r_4=\bar G_{15}d$，得到

$$
r_4=G_{15}d+Aq_4+pr_5.
$$

最后解 $\bar r_5=\bar G_{16}f$。由 $p^6T=0$，在完整系数扭子模中

$$
pb_j=\sum_{i=9}^{12}p^3g_i a_{ij}
+p^4g_{13}d_{13,j}+p^4g_{14}d_{14,j}
+p^5g_{15}f_{15,j}.
$$

这里索引从 0 开始。因此完整障碍矩阵为

$$
\mathcal O=\begin{bmatrix}
a_{9,*}\\a_{10,*}\\a_{11,*}\\a_{12,*}\\
d_{13,*}\\d_{14,*}\\f_{15,*}
\end{bmatrix}\in\mathbb F_{31}^{7\times9}.
$$

这七个 socle 方向独立。第 $j$ 列全零恰给最小指数 1；非零恰给最小指数 2。输出不是固定来源尝试的受限余量。

根 1 分量的最高系数指数为 2，而旧全原 $pb_j\in p^3C$ 已付，故该分量上的 $pb_j$ 为零；七个剩余 socle 方向全在根 2 分量。消费者仍保原 315 坐标及原 $s$ 作用，不以局部少数坐标代替完整像商。

## 3. 原整数符号与精度

新 native 每次重新生成原 $h_0$ 的 25 个整数系数，独立复乘四个已固定因子，核首项 3125；普通平方对角系数为 1，非对角为 2。全部来源使用原 6188 行和原 4367 输出。

其最终残量一律是 **target − A·source**。新输出 magic 为 R150TJ71/R150TR71，不能把它误称为纯 $A\kappa/p^e$。

五个原整数阶段依次为：

| 阶段 | target | source | 除数 | 计算/保真精度 |
|---|---|---|---|---|
| r3 | $pb$ | $Z$ | $p^3$ | 15/15 |
| 去前13类 | $p^2b$ | $pZ+\sum p^{4-e_i}\kappa_i a_i$ | $p^4$ | 15/15 |
| r4 | $p^2b$ | 上一 source $+p^4q_3$ | $p^5$ | 15/10 |
| 去前15类 | $p^2b$ | 上一 source $+\sum p^{5-e_i}\kappa_i d_i$ | $p^5$ | 10/10 |
| r5 | $p^2b$ | 上一 source $+p^5q_4$ | $p^6$ | 10/5 |

两次单位求解均核原 1034 行及全部 13 个自由条件，随后经原 V、逆 B、逆 F 运输到全部原 6188 来源，再重新按原 17 方程乘回。原模 31 根 2 最大参数指数 5 已付，因此每次有限单位解的形式延拓债为 5，形成 $15\to10\to5$。每个整数阶段仍检查其全部计算精度，没有把末五项补零当作已核。

每次 class 读取保留完整 820 状态、104 局部自由检查、39 重构、315 原扭子坐标、505 全局自由检查及原参数作用。有限局部 jet 的作用是确定完整局部系数模中的类；不声称保存的截断来源本身已经是全参数多项式恒等式。最终 membership 使用已付有限 $D$ 载体及其忠实分量完成。

## 4. 冻结源码

- runner：2026-11-16-r150-original-h0-seven-socle-runner-789f.py  
  blob 1809d2215b314bf3db7842aa24184a2b32c851ce  
  28094 bytes；SHA256 93f141b462521d09c35b70790ae862daad3e0ebdac1ee8642fec163a4e558bea
- native：2026-11-16-r150-original-h0-seven-socle-integer-p7-789f.cpp  
  blob dcef4573f3ecf4778e76b3d072fbee16a69f2cb4  
  21708 bytes；SHA256 f9c6c9f7576cfaa9d3c6bd46a0fdcee4dc414f2248ee4334700a1963a50dfd99
- 父 runner：2026-11-16-r150-root2-fourth-complete210-p7-runner-789f.py  
  blob 6b1c59588784109cd522c250db75699afdf61ff9  
  36750 bytes；SHA256 ad18b9749976bbc2c011575c29960709e0b954d54f3ef0cda75c8f4d126fc60d

其余 13 个 helper 及原 10 输入、6 小系统、5 原 source families、原 primitive、jet map、complete210 recipe 均沿父冻结 manifest，并由本 runner 全 SHA 重核。

## 5. 父子缓存身份

唯一接受的父 binding：

712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093

父 completed receipt 42372 bytes / dd867cfbbefcce2d7a846016807b1da6f56c73fd82ea9a364036348467bdc5b9；父 exact-result 141288 bytes / 30d9c04e68e337e2ac5019e527e97e211104b1e9276ff7caf24619a804fde8b9。

本次显式验证父 G/V 的完整物理 SHA、magic、shape 和父 binding，只把 header 的 64 个 binding 字节改为子 binding，其余数学 payload 逐字节相同。

父 L3/L4/L5/L6 列分别选 0 / 6,7,8,9 / 10,11 / 12。先验证整个父文件 SHA，随后逐原 6188 行验证 row header、选定系数及 EOF，写新 child SJ71。没有将父整数 source 直接作为未经验证的 child 输入。父 true13 坐标与实际 L3/L4 列逐项相等；true15 与原完整 incoming15 同 span；true16 全参数闭合。

新 q3/q4 及新 target-source 文件均由 child binding 生成。原全参数 polynomial 家族没有 pipeline binding，仍逐文件 SHA、全部原行和标签核验。

## 6. CLI 与续接

```bash
PYTHONPATH=/tmp/literature_root2_789f/python-deps python3 -u /tmp/literature_root2_789f/scripts/2026-11-16-r150-original-h0-seven-socle-runner-789f.py \
  --notes-root /tmp/literature_root2_789f/scripts \
  --parent-out /workspace/scratch/789f3e887d7c/literature_root2_789f_work/root2-fourth-complete210-p7 \
  --original-input-dir /workspace/scratch/789f3e887d7c/literature_root2_789f_work/global197-original-inputs \
  --small-input-dir /workspace/scratch/789f3e887d7c/literature_root2_789f_work/root2-fourth-small-inputs \
  --true-source-dir /workspace/scratch/789f3e887d7c/literature_root2_789f_work/root2-fourth-true-source-inputs \
  --exact-gzip /workspace/scratch/789f3e887d7c/literature_root2_789f_work/original127-inputs/original-primitive-integer-equations.json.gz \
  --jet-map-dir /workspace/scratch/789f3e887d7c/literature_root2_789f_work/root2-fourth-jet-map \
  --recipe /workspace/scratch/789f3e887d7c/literature_root2_789f_work/root2-fourth-complete210-preparation/complete210-fourth-source-recipes.json.gz \
  --out /workspace/scratch/789f3e887d7c/literature_root2_789f_work/original-h0-seven-socle \
  --seconds 1800 --memory-mib 4096 --through final
```

预算不进入 binding。预算暂停返回 75，同源同输入同 out 可以继续；完成阶段逐输出 SHA 复用，正在执行的 native 保存完整 source 前缀及部分原乘积。错误不当作数学否定。

本地已实际启动，执行身份 local-original-h0-seven-socle-20261116T044424Z；2026-11-16 04:44:25 UTC 观测正在运行。child binding dce92fb5bbd50efc3cf5bd39a5b7fbf27dec7f88e4c3e0b9308cfff47b042b98。此条只记录实际启动，不预填结果。

数学数组、所选原来源、完整结果 JSON 及日志均只在临时目录；仓库只收源码、参数、执行身份和实际输出 SHA。
