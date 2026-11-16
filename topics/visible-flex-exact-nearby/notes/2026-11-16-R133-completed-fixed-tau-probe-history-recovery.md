# R133：两份已完成fixed-tau浮点探针的原字恢复

2026-11-16。依根README12/15，普通删除两份可重复派生数据；完整证明、源、原输入定义、失败和Git历史保留。这里没有新数值，也没有把有限采样升级为连续认证。

恢复commit：`49fefaeb875a3a790c9d175212d409a2fe21e7e1`。未来消费者或原archive检查必须先从该commit在同path取回完整原字节，核Git blob/bytes/SHA，再读取；禁止重做旧探针。

| 原path（课题目录内） | Git blob | bytes | SHA256 |
|---|---|---:|---|
| notes/2026-11-12-D5-shared516-fixed-tau-forward-parameter-probe.json | 977dc3a01200790afe52a8f464af52151d1d0954 | 50356 | 4f0a0cfa20c4f87559e307d84c263d0bd7f73060d0be39ccd792c5ae9fb6154d |
| notes/2026-11-12-D5-shared516-fixed-tau-backward-parameter-probe.json | b6500295d3c3f253de012d14dbcc2113c0c6ce25 | 50324 | 1a807c09b7d950d6e9c5b6afae0f7de39147661f9f08897641a926ba320037bf |

完整小结论：`notes/2026-11-12-fixed-tau-parameter-reference-residual.md`，Git c141707aca066b911ec311a7ef6426c54d279809，7500B，SHA bae928ada4d6c0d0db84dae202f98233a6b658aa67ce4f465c0addc95a3a2a14。其§6保两腿完整已执行的7segments×3points×8rays范围、原命令、非零浮点缺陷和真实终点列。原source `scripts/fourfold_dense_fixed_tau_parameter_probe.py` SHA0137b012b719570b286cd52caea2be0d3f5681481942750e6b45d99207382882；原1133B manifest `notes/2026-11-12-fixed-tau-reference-identity-frozen-manifest.json` SHAedfd5a3b6689fb2b1de839fa702a33c9ea2ac70822362e331516b72cedf1bb73两项archive_required继续有效，只改为恢复后读取。

对象是原exact-affine δ3，不是本次selected成员。两份报告是对既有dense polynomial的派生采样；不是定义候选的系数。第二腿从第一腿完整native终点参数列入射，不是置零，也不依赖派生forward报告。原observed raw defects为4.6325787829432367e−14、6.838117678509123e−14，终点重构差均4.662069341687669e−17；全部原nonzero缺陷及限制照旧，绝不扣成认证余量。

这些2个path不在已完成WPTVS27current/19history、WMT9current及WRT七原actual的声明输入中；根只对这些具体文本/路径作有界检查，不声称所有历史源码无依赖。原F archive_required依赖明确保留。当前完整notes Git-tree元数据与恢复记录各显示100644/blob及同两身份；删除前再以fresh main guard验证。目标body、binary、native大文件读取0；科学执行0；无强推或历史改写。无额外独立审查/白名单审批要求。
