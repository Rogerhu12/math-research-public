# 按根规矩15移出一份可重算的旧 R168 数组报告

2026-11-20 09:44 UTC，Astra-larger-resume-24b2ab87-20261120。

本题当前受 Git 跟踪的文件为199909266 B，距离十进制200 MB上限只剩90734 B；为保存新的真实闭面求解源码，按根README第15条普通删除一份旧可重算输出，不改写历史。

唯一移出的路径是 `notes/2026-11-13-root-R168-M20-root-coordinates-r1.json`，993245 B，SHA256 `4d360e79d8e082786a73e7aa0d43c48391bcf7601011c8cdaafdf3d5d64d8fbf`。它是R168完整217个保存节点的坐标/根/诊断数组报告，不是作者源码或证明。R168的数学正文、原生成源码、输入manifest、launch-plan、resource与日志全部保留。

原生成器是 `computations/root_R168_M20_actual_root_coordinates.mjs`（源SHA `00123a49cb84baf5fb68f393d699b7a2774b11318405b1a4108b0db4c1a4cc88`）；参数为原M20、全部217节点、原quadrature512。完整参数/环境/输入身份见 `notes/2026-11-13-root-R168-launch-plan.json` 与 `notes/2026-11-13-root-R168-input-manifest.json`，后者原SHA `91353af602d3839514c143f2a2cf8a03c440d82e0d4b8b3adeb527935ffd981a`。原运行是11/13本地计算，不补造Actions run编号。

如旧R169/R177或其他历史消费者确需原完整逐字数组，使用固定历史恢复到scratch：

```sh
git show 2d56baaaa5811d345ff2e70fcc5b26e44e3d4823:topics/visible-flex-larger-amplitude/notes/2026-11-13-root-R168-M20-root-coordinates-r1.json > /tmp/R168-root-coordinates.json
```

先核上面的SHA，再把该消费者的本地输入路径指到恢复文件；不以不存在的当前路径或单个SHA假装有数据。历史manifest中的路径/数字作为历史记录保持，不声称这些消费者已经全部无引用或自动运行成功。

本次当前fullclosed恢复/求解不使用R168报告，其独立输入链在11/20恢复记录。此容量操作没有改变任何已证明/数值/失败结论，也没有重新计算R168。一次定位搜索不慎命中了旧报告的超长单行，工具输出已截断；未把截断内容当作完整科学输入，后续搜索限制行宽/文件大小。
