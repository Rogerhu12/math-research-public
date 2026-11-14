# R115：静态局部第四成本最高仿射权的准确支付与下一块边界

日期：2026-11-14。**准确公开代数回执与实现审计。** 本文只读取已经发布的四个小 JSON；没有在本地编译研究目标、评价 profile/几何或重新积分。不是完整第四周期、ruling 或有限等距族完成结论。

## 1. 本次身份与可复用输出

公开 run 为 **43645177423**，源提交为 **2f1b809c0b0abb7a26303d36940edc203815f872**。源码为 [literature_local_fourth_quotient.py](../scripts/literature_local_fourth_quotient.py)，38857 bytes，SHA256：

9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0

输出均在 [actions-43645177423-1-local_fourth_quotient](../notes/actions-43645177423-1-local_fourth_quotient/)。

| 文件 | bytes | SHA256 |
|---|---:|---|
| local-fourth-development.json | 3437 | 52ae4256bfc17410d2e75bf1bc5bd070878118fb416cb6dea86c6b0c0eef5c50 |
| local-fourth-quotient.json | 3982 | 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a |
| local-fourth-quotient-weight-+2.json | 4329 | 874c683855c9aef86a45602fc06cc3357fc5cff8bd7eeac64ecdae5150decd81 |
| local-fourth-quotient-weight-+1.json | 13499 | 57d8a80b8344f42cd8594e7d117d29098991d1c392d3101264195eeb1a8533c4 |

公开 job 先运行语法与人工检查。人工报告为 $0.00903966$ 秒、峰值 RSS $27.8984375$ MiB，completion 为 toy_passed。实际通过的人工门包括：真实 cov 求导后再置 history 值零、静态与正几何 jet 情形、非零 history 导数、R73 点态 trace 恒等、水平势、R109 的 $-1/6$ 因子，以及原始右 Volterra DAG 编解码。人工报告明确没有编译真实局部第四目标，也没有评价 profile 或几何。

### 原表达式导出已经完整发布

主 manifest 保留了下列原字节信息；大文件不通过 API 读取或切块传输，后继公开 Actions 直接消费。

| 导出 | gzip bytes / SHA256 | raw bytes / SHA256 | 内容 |
|---|---|---|---|
| local-fourth-quotient-W-original-expressions.json.gz | 7377 / 45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a | 31750 / 615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf | 完整 36 个原始 W 根，170 atoms |
| local-fourth-quotient-original-expressions.json.gz | 657195 / ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace | 3518194 / d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1 | 430 根，3319 atoms；W 加两个完整相位的静态局部密度 |

导出保存真正的原式 DAG，而不只是摘要 hash。W 的 36 个原 hash 与 v2 公开回执绑定；源码中的恢复过程先核全 152 个原模板。后继 m8 投影只消费 W，不需要重编彩色局部第三或任何旧 fourth forcing。

## 2. 已完成的准确代数范围

研究对象为 R109 的

$$
\mathscr L_4=v-\mathcal B_mN
$$

的**几何导数权零**部分；$v$ 先对真实场求导、代真实 history RHS，然后才把累计值置零。不是把 history 的导数也置零。

本次请求的 $+2,+1,0$ 是 profile 正仿射整权，不是几何导数权。R112 的几何导数权 $2,4$ 尚未计算；profile 权 $0$ 本次也没有执行，因为在首个未决块后停止。

两个完整相位模式 $-4,-2$ 使用同一实参数列，未各自配系数。

### 权 +2 已付

本块只有几何单项 $h^2k^2$。两列响应代表独立，给真实响应维数上界 $2$。该局部系数的准确原式身份为

$$
(\mathscr L_4^{[0]})_{h^2k^2,\,+2}
=-\frac18\,\mathcal B_{p_2}(W_7).
$$

这里 $W_7$ 是公开 v2 保留原索引 7、SHA 为
586788dc0fcf4aec7cc329277836c89e82ddb46a5739d71dfcd154cdece83a56
的完整第三模板。两模式均从原式重新组合检查为零。此正面身份不依赖“非零正规形代表一定独立”的假设。

### 权 +1 一根已付，两根未决

本块有八个原响应列，一条从原式重验的关系给真实响应维数上界 $7$。按报告列号，

$$
\mathrm{col}_6=-\mathrm{col}_1+\mathrm{col}_3.
$$

$h^2k^2\omega$ 的系数已付，两模式从原式回代均为零。其系数按列 $0,1,2,3,4$ 分别为

$$
-\frac14,\quad-\frac1{16},\quad-\frac18,\quad
\frac18,\quad-\frac1{16}.
$$

未决的是下列两根：

| 几何单项 | 改写后代表项数 | 余项数 | 余项 SHA256 |
|---|---:|---:|---|
| $hk$ | 260 | 206 | 239c9863d659e5381eb7d02d1353115607aaa1bd0c2998673caba678ac2afea7 |
| $hk^3$ | 261 | 206 | 7a56835e9ed7d31f8635d69cb61838f2cc72b46d581348977369b61dbaed3fd3 |

两份 preview 的开头相同，但完整余项 hash 不同；不能据截取的前 12 行把它们认作同一个函数或相反函数。该改写不是已证明完备的真实函数正规形，所以这里仅为 **identity_not_found**，未证明任何一个系数不属于响应空间。

此外，即便今后证明某个静态系数真非成员，也不能直接说它是可以独立调节的实际几何成本。完整 $M=0$ 路径把不同静态状态、正时长与连接耦合起来。R114 将处理这一步：应先对常态八矩的几何函数取约束商，再研究正配平的真实圈字。

## 3. output_limit 是报告接口缺陷

实际研究已写出两块 JSON 和两个完整导出。最后写主报告时，内存中的完整报告达到 **194340 bytes**，超过 CLI 指定的 95000-byte 上限。其 hash 为

84e68b1ff3cda4236cee2bbc4a7a995c19c5bc939c93e7d218c6aa6202cfda8d。

旧 write_report 只写了 3982-byte fallback，没有把这份完整 JSON 另存 gzip。因此主 completion 变为 output_limit；fallback 的 new_mathematical_conclusion=false 是保守格式字段，不能撤销已经单独发布、含原式零身份的完成块。另一方面，只有完整报告的 hash 也不能恢复其中未持久化的诊断细节。

本次没有必要重跑已完成 W、局部密度、+2 或原逐系数 +1 目标。下一 consumer 保留旧 producer 字节身份，直接绑定现有原式导出，并采用：

- 小主报告保存 scope、实际 completion、来源、完成块与完整报告文件元数据；
- 完整报告另存 gzip，记录 gzip/raw 的长度及 SHA；
- 先写已经完成的研究成果，再进入后续有预算的块；
- 每件与总输出均保留原体积门，不经 API 取大数据。

这修复的是落盘接口，不改变本次已发表原式或来源身份。

## 4. 继续范围

下一准确目标是同一 $\mathscr L_4^{[0]}$ 相对于常态八矩函数的受约束商，直接消费本次导出；不是扩大同一个未决正规化预算。W-only 同时可供完整 m8 响应投影消费。

本次未证明 $\mathcal U_4/\mathcal R_8$ 为零或非零，未支付实际第四成本半群、完整 ruling、无限阶收敛、闭曲面嵌入或 reach/宏观幅度门。
