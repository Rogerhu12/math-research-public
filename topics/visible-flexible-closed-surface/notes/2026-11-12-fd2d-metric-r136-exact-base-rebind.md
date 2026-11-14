# R171 准确 base 的原字节重用与实际新 bumps

## 1. 本次对象

R171 准确 profile 由固定 candidate、其准确 phase 积分及一组实际保存的 C4 bumps 组成：

$$
 a_\delta(s)=a_{\rm base}(s)+\sum_{j=1}^{7}\delta_j\psi_j(s).
\tag{1}
$$

固定 base 的准确 phase 长度、Taylor 积分系数、显式余项、累计半径和准确 cut 标签均已在 [原 R171 packet](2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz) 支付。本条只读取另一个实际 archive 中的七个 $\delta_j$、支持端点和独立参数布局；不重新积分 base，不把旧 $\delta$ 的 metric/posterior 复制为新目标的结果。

实际新输入为 [dyadic30 已接受场](2026-11-12-fd2d-raw-bump-dyadic30-trial-back01-a01-accepted.npz)，SHA256 为 3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981。其 131-node、31/16/7 布局和全部实际参数按保存字节消费；R170 尾域是完整角场读者的独立责任，标量 profile 不以 tail 系数正负推断角域合法性。

## 2. 准确重绑定命题

设原 packet 已严格包围准确 $a_{\rm base}$ 及所需一侧导数。若新 archive 满足：

1. candidate SHA、固定 $T$、物理 profile kind 与原 base 定义一致；
2. 保存的 mesh 有限、严格递增且起点为 0；
3. 独立中央/尾/profile 参数计数与总参数长度一致；
4. 每个新 bump 的支持严格避开准确中央柱和准确 cut 的邻域；
5. $\frac45+\sum_j\min(0,\delta_j)>0$；

则保留原 base 包围并按准确有理的新 $\delta_j$ 和支持端点加入 $\psi_j$ 及其导数，得到 (1) 的准确全片 profile 包围。证明仅用 R171 的准确 base 结论、C4 bump 的显式多项式和区间包含性。由于 $0\le\psi_j\le1$，第 5 条给出整域的正半径下界。因此 $a'/a$、$K=-a''/a$ 与所需一侧 $K_s$ 均可按同一新目标求值。

这是一条同 base 的新目标构造。若 $\delta$ 改变，(1) 通常改变，故其 input binding 必须改变。保留原累计积分并不意味着保存场、有限残差、frame/body 或任何完整后验相等。

## 3. 实现和精确运输

第一层 [fd2d_gc_r136_rebind_profile.py](../scripts/fd2d_gc_r136_rebind_profile.py) 使用原 R171 constructor 的实际检查方法绑定新的 archive；它显式核上述条件并核内存中 base 内容在重绑定前后没有改变。它保留实际 source/parent packet/field 身份和新参数的准确有理表示。

第二层 [fd2d_gc_r136_rebind_profile_v2.py](../scripts/fd2d_gc_r136_rebind_profile_v2.py) 直接从原 gzip packet 读取编码 JSON。以下 base 项原样复制：

~~~text
bundle, pieces, a0, end, central_length,
join_identities, precision, order
~~~

只更新输入身份、新 delta/support、field binding、完整 definition 和对应内容哈希。gzip 使用固定 mtime 0。写出后由原 R171 loader 重新载入，并核新 target binding、准确 bump 数值和 base 编码的内容哈希。

复制的是含准确有理端点的原 packet 数据，并非把 Arb 浮点中点重新取作准确数。这个实现也避免了无数学必要的重复 Taylor 求积。

完整 encoded base 的 SHA256 在父包和新包中完全相同：

~~~text
43dff49bbf7ebe82574c0a9644f895cc1e5d6ceacb362f1d1f4cb7aafb1d0b64
~~~

原准确 cut $S$ 保留；本条不把旧 binary64 最后节点 $E$ 自动认作 $S$。覆盖准确末格仍用 R172 或明确的 R170 适配。删柱包装也只能按准确坐标平移使用该对象。

## 4. 两次实际运行与首次失败

v1 进程 session 19435，首块 90fbd9、末块 7d243d，真实 exit 1，耗时 1.572090000998287 秒、峰 RSS 86504 KiB。[原失败报告](2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-01-report.json) 和已经输出的 packet 保留。失败来自过强的运输相等断言：Arb 解码再编码可把端点向外扩一小步，且 JSON 恢复的 list 与内存 tuple 不能靠 Python 容器相等判准确数相等。它不是发现 base 积分数学不成立，也不把失败改写成通过。

v2 独立源码通过原 encoded base 拷贝和准确数值编码比较修正这项运输检查。进程 session 87585，首块 4857bc、末块 2b9476，真实 exit 0，耗时 1.1114433539987658 秒、峰 RSS 86308 KiB。[实际通过报告](2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-report.json) 明确记录四个实际相等检查：

- 新 target binding 一致；
- 恢复的 decoded base 与原 loaded base 一致；
- 新 delta 的准确数值逐项一致；
- 新支持端点的准确数值逐项一致。

此外在物理 $s=7/10$ 查询一次新 $a,a_s,a_{ss},a_{sss},K,K_s$，以实际走到新参数切片；没有重复原 61 片积分或 130 点核验，没有运行全 F/J、BVP 或 body。

环境中断后，source、输入 archive、两份报告和两份 packet 均核回原 SHA。本文和闭存清单于恢复后补齐，不将文字补齐冒充另一次数学计算。

## 5. 闭存新目标

正式消费 v2 [新 packet](2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz)：

~~~text
compressed bytes = 381917
SHA256 = a6215af63b98cc8409faf9dbb46c039f86c1ef9e9bc6fedacdd62514ba3dcb5a
uncompressed bytes = 1394520
uncompressed SHA256 = 15fc63c9baf09dba3ce37d15cb43a59b630f3e6293e3e4127af6f0fc30d47dbf
new target binding = 5994cdb58d4d09a98e01dbd313b34480ed2eb89ced9a293c7d593d45ed276f7b
~~~

本次准确全域半径下界为

$$
 \frac{17637324711160292861}{23058430092136939520}>0.
$$

原 R171 loader 可直接加载此包；R175 Bernstein bump 后端可在不改 (1) 的前提下收紧局部范围。

在本课题目录重做时选择新的输出 stem：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d_gc_r136_rebind_profile_v2.py \
  --parent-packet notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz \
  --parent-sha256 7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c \
  --field notes/2026-11-12-fd2d-raw-bump-dyadic30-trial-back01-a01-accepted.npz \
  --out-prefix notes/2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-replay
~~~

完整 R170 角场必须另用声明该 domain packet 的 archive reader。本条不调用旧正系数 guard，也不宣称已经支付新30完整角/径向残差或闭曲面完成门。
